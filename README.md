# Spheronizator
Spheronizator is a Python research utility designed to voxelize protein structural data from existing PDB and mol2 files for use in machine learning training sets. The utility is intended to be a part of your data processing pipeline, with an interface that is convenient to use with [IPython](https://ipython.org/), [Jupyter](https://jupyter.org/), or similar. Please see the [detailed documentation](https://spheronizator.readthedocs.io/) for more information, usage, and examples.

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

## Alternative Installation (via Conda)

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

## Bugs and Issues
If you encounter any issues with the package, please report them through the [GitHub Issue Tracker](https://github.com/mattlrich/spheronizator/issues).

## Contributing
The project is happy to accept contibutions and enhancements. All contributions are to be made through GitHub pull requests. See [CONTRIBUTING](CONTRIBUTING.md) for more information.

## Contact
Matthew Richardson (richardson.m@ufl.edu)
Jose Cleydson (jferreiradasilva@ufl.edu)
Jose Cediel-Becerra (jcedielbecerra@ufl.edu)
Raquel Dias (raquel.dias@ufl.edu)

## License
Spheronizator is licensed under the [BSD 3-Clause License](https://choosealicense.com/licenses/bsd-3-clause/). Please see [LICENSE](LICENSE) for more information.
