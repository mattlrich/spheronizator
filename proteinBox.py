# Copyright (C) 2024 Matthew Richardson

import boxFunctions as box
import numpy as np
import re

class proteinBox:

    def __init__(self,atoms):

        # Input should be a list of Biopython atom objects and they should have their records updated with the corresponding mol2 file
        self.atoms=atoms
        
        # Load configuration file
        self._get_config()


    def buildData(self):
        
        # Extract coordinates from atom objects
        self._extract_coords()
        self._get_central_atoms()


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

        origin=[0,0,0] # Origin is zero for every *projected* box
        boxSize=self.config['boxSize']

        foundAtomsIndex=box.buildBox(origin,projectedAtoms,boxSize)

        return [self.atoms[i] for i in foundAtomsIndex]

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

            foundAtoms=self._build_box(centerAtom)
            filename_out="output/box" + str(index+1) + ".pdb"
            io.set_structure(structure)
            io.save(filename_out,boxSelect())
            print(filename_out)



