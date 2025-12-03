# Spheronizator
Spheronizator is a Python research utility designed to voxelize protein structural data from existing PDB files for use in machine learning training sets. The utility is intended to be a part of your data processing pipeline, with an interface that is convenient to use with [IPython](https://ipython.org/), [Jupyter](https://jupyter.org/), or similar. Please see the [detailed documentation](https://spheronizator.readthedocs.io/) for more information, usage, and examples.

<img src="workflow/spheronizator_workflow.png">

## Documentation
Detailed documentation for the project can be found here:
[https://spheronizator.readthedocs.io/](https://spheronizator.readthedocs.io/)

Documentation for the project is written in Markdown, rendered to a static site with [mdBook](https://rust-lang.github.io/mdBook/), and hosted by [Read the Docs](https://readthedocs.org/).

## Installation
The precompiled package is hosted on [PyPI](https://pypi.org/project/spheronizator/) and can be easily installed with pip:

```pip install spheronizator``` 

## Development
Packaging and building of the project is handled by [Poetry](https://python-poetry.org/docs/).

To install the development version, first install Poetry:

```pipx install poetry```

then clone the repository:

```git clone git@github.com:mattlrich/spheronizator.git```

then install the package in development mode to a virtual environment:

```poetry install```

You can build the source and wheels archives with:

```poetry build```

## Recommended Installation (via Conda)

If you prefer using **Conda** instead of Poetry or pip, you can install Spheronizator using a Conda environment.

```bash
# 1. clone the repository:
git clone https://github.com/Dias-Lab/spheronizator.git
cd spheronizator

# 2. create conda environment using yaml file and activate it. Use mamba instead of conda for faster installation:
   # with conda:
   conda env create -f spheronizator_env.yml
   conda activate spheronizator

# 3. install the python package
pip install -e .
```

## Usage
To show SpheronizaTor arguments:

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

To run SpheronizaTor for a protein file:

```text
voxelize tests/sampledata/1YU6_A.pdb
```

## 💾 Outputs

The pipeline produces three main directories:

- **`metadata/`**  
  Contains a `.tsv` file summarizing the metadata for each residue, including:
  - Box index  
  - Residue index  
  - Residue label  

- **`output_vox_atoms/`**  
  Contain a NumPy `.npy` file representing the **atom-level voxelized features** for each residue.

- **`output_vox_bonds/`**  
  Contains a NumPy `.npy` file representing the **bond-level voxelized features** for each residue.

## Bugs and Issues
If you encounter any issues with the package, please report them through the [GitHub Issue Tracker](https://github.com/mattlrich/spheronizator/issues).

## Contributing
The project is happy to accept contibutions and enhancements. All contributions are to be made through GitHub pull requests. See [CONTRIBUTING](CONTRIBUTING.md) for more information.

## Contact
- **Matthew Richardson** — richardson.m@ufl.edu
- **Jose Cleydson** — jferreiradasilva@ufl.edu
- **José Cediel-Becerra** — jcedielbecerra@ufl.edu
- **Raquel Dias** — raquel.dias@ufl.edu

## License
Spheronizator is licensed under the [BSD 3-Clause License](https://choosealicense.com/licenses/bsd-3-clause/). Please see [LICENSE](LICENSE) for more information.
