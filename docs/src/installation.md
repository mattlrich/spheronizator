# Installation
There are a number of ways to go about installing and using this package. A sensible way to use this package is to create a conda environment for it, then install the package to that conda environment with pip. You may also use Poetry to facilitate installing the package to a virtual environment, which I recommend.

## Dependencies
Spheronizator has limited dependencies which will be automatically installed by using Pip or Poetry.

| Package | Version | Notes |
|----------|---------|----------|
| [Biopython](https://biopython.org/wiki/Download) | 1.85 | Development was done on version 1.81, but the package has been tested on 1.85
| [Numpy](https://numpy.org/install/) | 1.26.4 | Package has not been tested on Numpy 2.0


## Package Manager
Spheronizator is available in [PyPI](https://pypi.org/) and can easily be installed with pip.

```bash
pip install spheronizator
```

### Using a Conda Environment
If you prefer to install the package into a Conda environment, you can use the configuration from the repository.

First download the configuration:
```
curl -L -o spheronizator_env.yml https://raw.githubusercontent.com/dias-lab/spheronizator/refs/heads/main/spheronizator_env.yml
```

Now create a Conda environment using the configuration:
```
conda env create -f spheronizator_env.yml
```
```
conda activate spheronizator
```

You can now install the package into the environment with pip:
```
pip install spheronizator
``` 

## Install Development Version from Source
Spheronizator package management is handled by [Poetry](https://python-poetry.org/docs/), which also provides a convenient way to install the source into a virtual environment.

First install Poetry if you don't already have it:

```
pipx install poetry
```

then clone the repository:

```
git clone git@github.com:dias-lab/spheronizator.git
```

then install the package in development mode to a virtual environment:

```
poetry install
```

You can build the source and wheels archives with:

```
poetry build
```
