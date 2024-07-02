# Copyright (C) 2024 Matthew Richardson

'''
The goal of this parser is to maintain interoperability with Biopython's parsing of PDB files while adding information within mol2 files to Biopython structure objects.

'''

import numpy as np
from Bio.PDB.PDBParser import PDBParser
import re

class mol2parser:
    
    def __init__(self):
        self.parsedData=[]
        self.sections=[]
        self.atoms=[]

    def parse_mol2(self, file):
        
        with open(file, 'r') as mol2file:
            
            sectionCounter=-1
        
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
                            
                    
    def get_atoms(self):
        
        return self.parsedData[self.sections['ATOM']][1:]

    def parse_pdb(self, file):

        pdb=PDBParser()
        structure=pdb.get_structure(file, file)
        
        for residue in structure.get_residues():
            for index,atom in enumerate(residue.get_atoms()):
                if index==0:
                    atom.central=True
                else: 
                    atom.central=False

                self.atoms.append(atom)

    def update_records(self):

        mol2atoms=self.get_atoms()

        for i in range(len(self.atoms)):
            self.atoms[i].detailedAtomType=mol2atoms[i][5]

        


