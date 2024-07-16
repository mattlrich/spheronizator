# Copyright (C) 2024 Matthew Richardson

import boxFunctions as box
import numpy as np
import re
from mol2parser import mol2parser

class proteinBox:

    def __init__(self, config=None):
        
        # Load configuration file
        self._get_config(config)


    def parse(self, pdbfile, mol2file=None):

        # Wrapper for mol2parser. Adds method to proteinBox object to simplify interface.

        parser=mol2parser(pdbfile, mol2file)    # Create instance of parser object
        self.atoms=parser.atoms
    
    def buildData(self):
        
        self._get_central_atoms()               # Get our central atoms, one for each residue
        self._get_voxels()                      # Generate our voxels we will need for each box and store as object attribute

        # Get output array ready
        
        boxSize=self.config['boxSize']+1

        self.output=np.zeros((
                len(self.centralAtoms),         # Number of residues
                boxSize,                        # Box size
                boxSize,
                boxSize,
                5                               # Number of features
                ), dtype=int)
        
        for i in range(len(self.centralAtoms)):
            foundAtoms, foundAtomIndices, projectedCoords=self._build_box(self.centralAtoms[i])
            array=self._process_box(foundAtomIndices, projectedCoords)
            
            self.output[i]+=array
               

    def _get_config(self,configPath=None):

        if configPath is None:
            configPath='config'

        try:
           with open(configPath, 'r') as configFile:
                
                config=[]
                delimiter=re.compile(r'=')

                for line in configFile:
                    
                    line=line.strip()

                    if line and not line.startswith('#'):
                        config.append(delimiter.split(line))
                
                for i in range(len(config)):
                    config[i][1]=int(config[i][1])

                self.config=dict(config)

        except:
            print("\nConfigation file was unable to be parsed, applying defaults.")

    
    def _get_central_atoms(self):

        self.centralAtoms=[]

        for atom in self.atoms:
            if atom.isAA and atom.isCentral:
                self.centralAtoms.append(atom)
    
    def _extract_coords(self):
        
        self.centralCoords=[]
        self.atomCoords=[]

        for atom in self.atoms:
            if atom.isAA and atom.isCentral:
                self.centralCoords.append(atom.get_coord())

            self.atomCoords.append(atom.get_coord())

        self.centralCoords=np.array(self.centralCoords, dtype=np.float32)
        self.atomCoords=np.array(self.atomCoords, dtype=np.float32)

    def _build_box(self, centerAtom):

        ## Give the function a center atom object to build the box about

        # Get parent residue of center atom
        residue=centerAtom.get_parent()

        # Obtain coordinate projection of all atom objects about a standard position based on the parent residue
        projectedAtoms=box.get_boxProjection(residue,self.atoms)

        origin=(0,0,0) # Origin is zero for every *projected* box
        boxSize=self.config['boxSize']

        foundAtomIndices=box.buildBox(origin,projectedAtoms,boxSize)

        foundAtoms=[self.atoms[i] for i in foundAtomIndices]

        return foundAtoms, foundAtomIndices, projectedAtoms
                
    def _get_voxels(self):

        # Generate the voxels we will need for the whole structure. Voxels are not unique to each box, so they only need to be generated once.
        
        boxSize=self.config['boxSize']
        voxelSpacing=self.config['voxelSpacing']

        self.voxels=box.get_voxels(boxSize,voxelSpacing)

    def _process_box(self, foundAtomIndices, projectedCoords):
        
        array=np.zeros((self.output.shape[1:]), dtype=int)
       
        atomTypeDict={
                    'C':0,
                    'N':1,
                    'O':2,
                    'P':3,
                    'S':4
                }

        for i in foundAtomIndices:
            atom=self.atoms[i]
            voxelIndex, voxelCoords=box.get_closestVoxel(projectedCoords[i], self.voxels)
            
            try:
                typeHeavyAtomIndex=atomTypeDict[atom.atomType]
            except:
                continue

            array[voxelIndex][typeHeavyAtomIndex]=1

            return array


    def _debug_export_boxes(self,structure):

       # This function is used to export generated boxes into a directory as PDB files themselves for testing/debugging purposes. 
        
        from Bio.PDB.PDBIO import Select
        from Bio.PDB import PDBIO

        io=PDBIO()
        
        class boxSelect(Select):
            def accept_atom(self, atom):
                if atom in foundAtoms:
                    return True
                else:
                    return False

        for index,centerAtom in enumerate(self.centralAtoms):

            foundAtoms, foundAtomsIndex, projectedCoords=self._build_box(centerAtom)
            filename_out="output/box" + str(index+1) + ".pdb"
            io.set_structure(structure)
            io.save(filename_out,boxSelect())
            print(filename_out)



