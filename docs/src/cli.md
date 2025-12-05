# Command Line Interface

Spheronizator now includes a command line interface contributed by Dr. Raquel Dias and José Cediel-Becerra.

The command line interface allows generation of static data files from provided PDB files.

## Usage

The command line interface can be invoked by running the following command:
```text
voxelize -h
```
```
usage: voxelize [-h] [--voxel_spacing VOXEL_SPACING] [--use_float_voxels USE_FLOAT_VOXELS] [--box_size BOX_SIZE] [--use_spheres USE_SPHERES]
                [--data_type DATA_TYPE] [--overwrite] [--atom_out_dir ATOM_OUT_DIR] [--bond_out_dir BOND_OUT_DIR] [--meta_out_dir META_OUT_DIR]
                pdb_file

Extract voxel boxes/spheres from a protein PDB file

positional arguments:
  pdb_file              Protein PDB file to process

options:
  -h, --help            show this help message and exit
  --voxel_spacing VOXEL_SPACING
                        Voxel spacing (default: 0.5)
  --use_float_voxels USE_FLOAT_VOXELS
                        Use float voxels (default: True)
  --box_size BOX_SIZE   Box size (default: 20)
  --use_spheres USE_SPHERES
                        Use spheres (default: True)
  --data_type DATA_TYPE
                        Data type (default: float16)
  --overwrite           Overwrite existing outputs if present
  --atom_out_dir ATOM_OUT_DIR
                        Directory for atom voxel outputs (default: ./output_vox_atoms)
  --bond_out_dir BOND_OUT_DIR
                        Directory for bond voxel outputs (default: ./output_vox_bonds)
  --meta_out_dir META_OUT_DIR
                        Directory for metadata outputs (default: ./metadata)
```

### Examples

To run Spheronizator on a protein file:
```text
voxelize tests/sampledata/1YU6_A.pdb
```

## Outputs

The utility produces three main directories:

- **`metadata/`**  
  Contains a `.tsv` file summarizing the metadata for each residue, including:
  - Box index  
  - Residue index  
  - Residue label  

- **`output_vox_atoms/`**  
  Contain a NumPy `.npy` file representing the **atom-level voxelized features** for each residue.

- **`output_vox_bonds/`**  
  Contains a NumPy `.npy` file representing the **bond-level voxelized features** for each residue.