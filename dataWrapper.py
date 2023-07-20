import pandas as pd
import numpy as np
import box_algorithm as box
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import is_aa

# Let Biopython handle parsing the PDB files
file='demo.protein.pdw'
parser=PDBParser()
structure=parser.get_structure("my first protein", file)

atoms=[]
centralAtoms=[]
for residue in structure.get_residues():
    # Make sure the residue is an amino acid
    if is_aa(residue):
        for index,atom in enumerate(residue.get_atoms()):
            if index==0: centralAtoms.append(atom.get_full_id())
            atoms.append(atom.get_full_id())

print(atoms[0][1])
print(len(centralAtoms))

# Try getting the coordinates of our central atoms
coordinates=[atom.get_coordinates() for atom in centralAtoms]
print(coordinates)

## May want to read Biopython 11.6.4.5 for a more efficient implementation