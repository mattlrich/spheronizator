# Copyright (C) 2024 Matthew Richardson

import boxFunctions as box
import numpy as np
import re
from mol2parser import mol2parser

class proteinBox:

    def __init__(self, config=None):
        
        # Load configuration file
        self._get_config(config)

        self.bondTypeDict={
                '1':0,
                '2':1,
                '3':2,
                'am':3,
                'ar':4
                }

        self.atomTypeDict={
                'H':0,
                'C':1,
                'N':2,
                'O':3,
                'P':4,
                'S':5
                }

    def parse(self, pdbfile, mol2file=None):

        # Wrapper method for mol2parser class. This simplifies the interface.

        parser=mol2parser(pdbfile, mol2file)    # Create instance of parser object, parse and update atom objects
        self.structure=parser.structure
        self.residues=parser.residues

        # Only get atoms that belong to amino acids
        self.atoms=[atom for atom in parser.atoms if atom.isAA]

        self._get_resnames()
    
    def buildData(self):
        
        self._get_voxels()                      # Generate our voxels we will need for each box and store as object attribute
        self._init_arrays()                     # Initialize all arrays we will need for output data

        for i in range(len(self.residues)):
    
            # Build data for atom abscence / presence
            foundAtomIndices, projectedCoords=self._build_box(self.residues[i])
            boxArray=self._process_box(foundAtomIndices, projectedCoords, i)
            
            self.output[i]+=boxArray

            # Build data for bond information
            self._process_box_bonds(foundAtomIndices, i)
               
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
                
                
                self.config=dict(config)

        except:
            print("\nConfigation file was unable to be parsed, applying defaults.")

            self.config={
                        'boxSize':20,
                        'voxelSpacing':1,
                        'useFloatVoxels':False
                    }

        # Unpack values to attributes. This allows this values to be changed after initialization.
        self.boxSize=int(self.config['boxSize'])
        self.voxelSpacing=int(self.config['voxelSpacing'])
        self.useFloatVoxels=bool(self.config['useFloatVoxels'])
    
    def _init_arrays(self):
        
        boxSize=self.boxSize+1
        residueCount=len(self.residues)

        # Output array for heavy atom presence / abscence
        self.output=np.zeros((
                residueCount,                   # Number of residues
                boxSize,                        # Box size
                boxSize,
                boxSize,
                len(self.atomTypeDict)          # Size of atomTypeDict representing the number of atom channels
                ), dtype=int)

        self.outputBonds=np.zeros((
                residueCount,
                len(self.bondTypeDict)
                ), dtype=int)
    
    def _get_resnames(self):

        self.resnames=[residue.get_resname() for residue in self.residues]
    
    def _extract_coords(self):
        
        self.centralCoords=[]
        self.atomCoords=[]

        for atom in self.atoms:
            if atom.isAA and atom.isCentral:
                self.centralCoords.append(atom.get_coord())

            self.atomCoords.append(atom.get_coord())

        self.centralCoords=np.array(self.centralCoords, dtype=np.float32)
        self.atomCoords=np.array(self.atomCoords, dtype=np.float32)

    def _build_box(self, residue):

        ## Give the function a residue to build the box about

        # Obtain coordinate projection of all atom objects about a standard position based on the parent residue
        projectedAtoms=box.get_boxProjection(residue, self.atoms)

        origin=(0,0,0) # Origin is zero for every *projected* box

        # Get the indices of all atoms contained within the box
        foundAtomIndices=box.buildBox(origin, projectedAtoms, self.boxSize)

        return foundAtomIndices, projectedAtoms
                
    def _get_voxels(self):

        # Generate voxels and store as attribute.  Voxels are not unique to each box, so they only need to be generated once.
        if self.useFloatVoxels:
            self.voxels=box.get_floatVoxels(self.boxSize, self.voxelSpacing)

        else:
            self.voxels=box.get_voxels(self.boxSize, self.voxelSpacing)

    def _process_box(self, foundAtomIndices, projectedCoords, residueIndex):
        
        boxArray=np.zeros((self.output.shape[1:]), dtype=int) 

        for i in foundAtomIndices:
            atom=self.atoms[i]
            voxelIndex, voxelCoords=box.get_closestVoxel(projectedCoords[i], self.voxels)
            
            try:
                typeHeavyAtomIndex=self.atomTypeDict[atom.atomType]
            except:
                continue

            if atom.isAA and atom.residueIndex==residueIndex:
                boxArray[voxelIndex][typeHeavyAtomIndex]=-1

            else:        
                boxArray[voxelIndex][typeHeavyAtomIndex]=1

            return boxArray

    def _process_box_bonds(self, foundAtomIndices, residueIndex):
        
        mol2indices=[self.atoms[i].mol2atomIndex for i in foundAtomIndices]
        
        for i in foundAtomIndices:
            
            atom=self.atoms[i]

            if hasattr(atom, 'bondData'):
                for bond in atom.bondData:
                    if bond[0] in mol2indices:
                        try:
                            bondIndex=self.bondTypeDict[bond[1]]

                        except:
                            continue

                        self.outputBonds[residueIndex][bondIndex]+=1

    
    def _debug_export_boxes(self):

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

        for index,residue in enumerate(self.residues):

            foundAtomsIndex, projectedCoords=self._build_box(residue)
            foundAtoms=[self.atoms[i] for i in foundAtomsIndex]
            filename_out="output/box" + str(index+1) + ".pdb"
            io.set_structure(self.structure)
            io.save(filename_out,boxSelect())
            print(filename_out)



