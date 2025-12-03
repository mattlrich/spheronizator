from setuptools import setup, find_packages

VERSION = "0.1.0"
DESCRIPTION = "spheronizator"

setup(
    name="spheronizator",
    version=VERSION,
    description=DESCRIPTION,
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "voxelize = spheronizator.voxelize:main",
        ],
    },
)
