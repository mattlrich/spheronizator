# Copyright (C) 2024 Matthew Richardson

'''
The goal of this parser is to maintain interoperability with Biopython's parsing of PDB files while adding information within mol2 files to Biopython structure objects.

'''

import numpy as np
from Bio.PDB.PDBParser import PDBParser
import re

class mol2parser:
    
    def __init__(self):
        pass

    def parse(self,file):

        try:
            self._parse_pdb(file)
            self._parse_mol2(file+'.mol2')
        
        except ParseError:
            print("Files were unable to be parsed")

    def update_records(self):

        try:
            self._add_detailed_atom_type()
            self._add_bond_info()
        
        except ParseError:
            print("Unable to update atomic records from mol2 file")

    def _parse_pdb(self, file):

        pdb=PDBParser()
        structure=pdb.get_structure(file, file)
        
        self.atoms=[]
        
        for residue in structure.get_residues():
            for index,atom in enumerate(residue.get_atoms()):
                if index==0:
                    atom.central=True
                else: 
                    atom.central=False

                self.atoms.append(atom)

    def _parse_mol2(self, file):
        
        with open(file, 'r') as mol2file:
            
            sectionCounter=-1
            self.sections=[]
            self.parsedData=[]
            delimiter=re.compile(r'\s+')
            
            for line in mol2file:

                line=line.strip()
                
                if line.startswith('@<TRIPOS>'):
                    sectionCounter+=1
                    self.parsedData.append([line.removeprefix('@<TRIPOS>')])
                    sectionName=self.parsedData[sectionCounter][0]
                    self.sections.append([sectionName,sectionCounter])
            
                elif line:
                    line=delimiter.split(line)      
                    self.parsedData[sectionCounter].append(line)

            self.sections=dict(self.sections)
                            
                    
    def _get_atoms(self):
        
        return self.parsedData[self.sections['ATOM']][1:]

    def _get_bonds(self):

        return self.parsedData[self.sections['BOND']][1:]

    def _add_detailed_atom_type(self):

        # Update the atom objects extracted from the PDB file with information from the corresponding mol2 file

        mol2atoms=self._get_atoms()

        for i in range(len(self.atoms)):
            self.atoms[i].detailedAtomType=mol2atoms[i][5]

        
    def _add_bond_info(self):

        mol2bonds=self._get_bonds()

        for bond in mol2bonds:
            
            originID, targetID, bondType=int(bond[1]), int(bond[2]), bond[3]
            originIndex=originID-1

            # sanity check

            if not originID==self.atoms[originIndex].get_serial_number():
                print(originID,self.atoms[originIndex].get_serial_number())
                raise ValueError

            # Test to see if the atom object already contains the bondData attribute
            if not hasattr(self.atoms[originIndex],'bondData'):
                self.atoms[originIndex].bondData=[]

            self.atoms[originIndex].bondData.append([targetID,bondType])

