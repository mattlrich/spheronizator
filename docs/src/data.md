# Data Files
Spheronizator requires data files to be able to operate. It requires both:
1. A PDB file
2. A corresponding mol2 file

## PDB Files
PDB files (Protein Data Bank files) are a standard molecular file format. These can be exported from many compatible pieces of software. You will need to provide at least one PDB file to Spheronizator to have data to process.

PDB files can be sourced for free from the [Protein Databank](https://www.rcsb.org/), licensed under [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).

## Mol2 Files
mol2 files are a less common format but can be generated automatically from existing PDB files with the open source utility [Open Babel](https://openbabel.org/).

With Open Babel, a PDB file can be converted to mol2 with the following command:
```
obabel -ipdb -omol2 protein.pdb -o protein.mol2
```
Please see the [Open Babel Documentation](https://openbabel.org/docs/) for more information.