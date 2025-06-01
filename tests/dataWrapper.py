# Copyright (C) 2024 Matthew Richardson

import pandas as pd
import numpy as np
import boxFunctions as box
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import is_aa
from mol2parser import mol2parser

# Let Biopython handle parsing the PDB files
file='testing_set/1YU6_C.pdb'
parser=PDBParser()
structure=parser.get_structure("my very first protein", file)
residues=structure.get_residues()

# Parse the corresponding mol2 file to grab some extra information
mol2file=file+".mol2"
mol2parser=mol2parser()
mol2parser.parse(mol2file)
mol2atoms=mol2parser.get_atoms()

# Extract Atoms from the structure. We will need to refer back to them later.
# This currently uses the Nitrogen as the center of each amino acid.
atoms=[]
centralAtoms=[]
for residue in residues:
    if True: #is_aa(residue): # Make sure the residue is an amino acid
        for index,atom in enumerate(residue.get_atoms()):
            if index==0: centralAtoms.append(atom)
            atoms.append(atom)

    

# Extract Coordinates from Atom Objects
centralCoords=np.array([atom.get_coord() for atom in centralAtoms], dtype=np.float32)
atomCoords=np.array([atom.get_coord() for atom in atoms], dtype=np.float32)
#structureLimits=box.get_structureLimits(atomCoords)
#samplePoints=box.get_samplePoints(structureLimits,1)







## May want to read Biopython 11.6.4.5 for a more efficient implementation
