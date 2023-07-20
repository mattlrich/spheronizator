import pandas as pd
import numpy as np
import box_algorithm as box
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import is_aa

# Let Biopython handle parsing the PDB files
file='demo.protein.pdw'
parser=PDBParser()
structure=parser.get_structure("my very first protein", file)

# Extract Atoms from the structure. We will need to refer back to them later.
atoms=[]
centralAtoms=[]
for residue in structure.get_residues():
    if is_aa(residue): # Make sure the residue is an amino acid
        for index,atom in enumerate(residue.get_atoms()):
            if index==0: centralAtoms.append(atom)
            atoms.append(atom)

# Extract Coordinates from Atom Objects
centralCoords=[atom.get_coord() for atom in centralAtoms]
atomCoords=[atom.get_coord() for atom in atoms]
#print(centralCoords[0])

# Run box generation algorithm
for index,centralAtom in enumerate(centralCoords):
    inRange=box.buildBox(centralAtom, 5, 1, atomCoords)
    print(index,inRange)
    

## May want to read Biopython 11.6.4.5 for a more efficient implementation
