# Getting Started
Using the package should be straightforward as the interface is designed to fit comfortbly into the typical workflow in the field using the IPython interpreter, either standalone or in Jupyter.

A Jupyter notebook with the following example can be found [here](https://github.com/mattlrich/spheronizator/blob/main/examples/demo.ipynb).

## Importing
First import the package:
```
import spheronizator as sp
```
This allows you to create instances of the voxelBuilder class, which is the heart of the package.

As an example, create a new voxelBuilder object called *x*.
```
x=sp.voxelBuilder()
```

## Configuration

When you call a new instance of the voxelBuilder class, it accepts 1 argument, *config*, which is the path to an optional configuration file. This file stores the default configuration and one is provided to you in the directory to work with. The argument allows you to specify a different configuration file.

```
x=sp.voxelBuilder(~/path/to/config/testing.config)
```

### Configuration Attributes
It is not necessary to use the configuration file to change the settings.

Optionally, you can update the settings by changing the object's attributes on-the-fly. It's not necessary to change or load different configation files every time.

See the [configuration](configuration.md) documentation for more details.

As an example, we can update the following three attributes:

```
x.boxSize=20
x.voxelSpacing=1
x.useFloatVoxels=True
```

## Loading Protein Data

To load protein data, you will need to parse both a PDB and corresponding mol2 file. Parsing of both of these file types is handled separately by the mol2parser class which is provided by the package.

To simplify the interface of this project, a wrapper for the mol2parser class is included as a method for the voxelBuilder class. This method prevents you from needing to interact with the mol2parser class at all; however, the mol2parser class can be used as a standalone parser for other projects if needed.

### Using the wrapper

Using the parser method is simple. Simply call the `parse` method with 1 argument specifying the path to a PDB file:

```
x.parse('testing_set/1YU6_C.pdb')
```

By default, the parser looks in the same directory for the corresponding mol2 file. The mol2 file must have the same name, plus the extension *.mol2*. This way you won't need to specify both PBD and mol2 files, just the PDB file if they follow this naming scheme.

If needed, a second argument specifies the corresponding mol2 file:

```
x.parse('testing_set/1YU6_C.pdb', 'testing_set/1YU6_C.pdb.mol2')
```
### Parsing Details
The parser will parse the specified PDB file and from it extract a list of atom objects. The parser then parses the corresponding mol2 file and updates the atom objects with additional data. The residues and atom objects are then all stored as attributes of the voxelBuilder class.

```
x.structure
x.residues
x.atoms
x.resnames
```

## Atom Objects
Biopython atom objects are the core data type for this project. You can learn more about Biopython atom objects by reading the [Biopython documentation](https://biopython.org/wiki/Documentation). The attributes of each Biopython atom object are updated with data extracted from the associated mol2file. A list of these attributes follows.

```
atom.bondData
atom.isAA
atom.detailedAtomType
atom.atomType
atom.residueIndex
atom.mol2atomIndex
```

## Building Output Array Data
Building the output array is as simple as invoking the `buildData` method as follows. This presupposes that the data has already been parsed. This method, in order:
1. Generates the voxel array that we will need based on the configuration parameters `boxSize` and `voxelSpacing`. The voxels are not unique to each residue, so the same voxel array is used for all residues in the protein. The generated voxel array can be found under the attribute `.voxels`
2. Initializes Numpy arrays of zeros for our output data with the appropriate shape. Currently two arrays are created:
    - *voxelBuilder.output* for atom presence / abscence
    - *voxelBuilder.outputBonds* for count of certain types of bonds within each box
3. Iterates through each residue computing data for each and updating the output arrays.

Once the output arrays are built, they can then be saved using any external tool of your choice, or immediately processed by the remainder of your data processing toolchain.