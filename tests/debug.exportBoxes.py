import numpy as np
import boxFunctions as box
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import is_aa
from Bio.PDB.PDBIO import Select
from Bio.PDB import PDBIO


'''
This script is used to import a PDB file using Biopython, and generate a set of boxes for each central amino acid based on the given parameters. Boxes are exported to a directory as PDB files themselves for testing/debugging purposes. This script is old and will not be updated. You may need to use the 2023 version of boxFunctions.py to get it to work.

'''

# Let Biopython handle parsing the PDB files
parser=PDBParser()
io=PDBIO()

file='demo.protein.pdw'
structure=parser.get_structure("my very first protein", file)

# Class is used to select atoms for output in the structure
class boxSelect(Select):
    def accept_atom(self, atom):
        if atom in writeOut:
            return True
        else:
            return False

# Extract Atoms from the structure. We will need to refer back to them later.
atoms=[]
centralAtoms=[]
for residue in structure.get_residues():
    if is_aa(residue): # Make sure the residue is an amino acid
        for index,atom in enumerate(residue.get_atoms()):
            if index==0: centralAtoms.append(atom)
            atoms.append(atom)

# Extract Coordinates from Atom Objects
centralCoords=np.array([atom.get_coord() for atom in centralAtoms], dtype=np.float32)
atomCoords=np.array([atom.get_coord() for atom in atoms], dtype=np.float32)

for index,atom in enumerate(centralAtoms):
    residue=atom.get_parent()
    projectedAtoms=box.get_boxProjection(residue,atoms)
    
    # Origin is zero for every *projected* box
    foundAtoms=box.buildBox([0,0,0],projectedAtoms,10)

    writeOut=[atoms[x] for x in foundAtoms]
                
    filename_out="output/box" + str(index+1) + ".pdb"
    io.set_structure(structure)
    io.save(filename_out,boxSelect())
    print(filename_out)


    
    
