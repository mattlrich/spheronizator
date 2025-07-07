# The *voxelBuilder* class

The *voxelBuilder* class is the primary interface for spheronizator.

## Methods
#### `voxelBuilder.reloadConfig(configPath=None)`
Parse a configuration file at a provided path, then update attributes.

#### `voxelBuilder.parse(pdbfile, mol2file=None)`
Parse protein data from a given PDB file and mol2 file. The mol2 file and PDB file must be for the same protein.

By default, the mol2 file is treated as having the same naming convention as the PDB file. As an example, the command

```python
voxelBuilder.parse(protein_data.pdb)
```

will look for files with the naming scheme

*protein_data.pdb*

*protein_data.mol2*

### `voxelBuilder.buildData()`
Initializes voxel arrays, output arrays, and then builds the output array. Does not take any arguments.

### `voxelBuilder.check_collision()`
Returns True if there has been a collision of two or more atoms located at a specific voxel. Datatype for the output array must not be boolean.

### `voxelBuilder.find_collision()`
Returns the indicies of the output array where two or more atoms have been represented by a single voxel. Dataype must not be boolean.

## Attributes
### `.config`
Configuration attribute. See [configuration](configuration.md).

### `.boxSize`
Configuration attribute. See [configuration](configuration.md).

### `.voxelSpacing`
Configuration attribute. See [configuration](configuration.md).

### `.useFloatVoxels`
Configuration attribute. See [configuration](configuration.md).

### `.dataType`
Configuration attribute. See [configuration](configuration.md).

### `.useWarnings`
Configuration attribute. See [configuration](configuration.md).

### `.useSpheres`
Configuration attribute. See [configuration](configuration.md).

### `.bondTypeDict`
Dictionary defining the mapping between types of bonds and their locations in the output array.

### `.atomTypeDict`
Dictionary defining the mapping between types of atoms and their locations in the output array.

### `.structure`
Biopython structure object of the parsed protein.

### `.residues`
List of Biopython residue objects located in the structure.

### `.atoms`
List of Biopython atom objects located in the structure.

### `.resnames`
List of all residue names located in the structure.

### `.voxels`
Voxel array which is used to check spatial presence of atoms in the structure. This array should not be changed by hand. It is initialized automatically based on the configuration settings when building the output array.

### `.output`
Output numpy array consisting of the final processed data.

### `.outputBonds`
Bond information array, part of the final processed data.




