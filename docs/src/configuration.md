# Configuration
It is not necessary to use a configuration file to adjust the parameters of the utility. It is possible to update all configuration parameters by adjusting the values of the corresponding attributes after initializing a new instance of the `voxelBuilder` class.

The configuration file simply selects the starting values these attributes will be initialized with when creating a new instance of the `voxelBuilder` class.

The configuration file supports the following parameters.

| Parameter | Type | Description |
|-----------|---------|-------------|
| boxSize | float | The dimensions of the output array. If boxes are used, this will be the length of one of the edges. If spheres are used, this will be the diameter of the sphere. Keep in mind since the origin is included, a boxSize of 20 with 1 angstrom spacing will produce a 20 angstrom box with an array size of 21x21x21.|
| voxelSpacing | float | Distance between each of the voxels in angstroms.|
| useFloatVoxels | bool | Whether or not to generate the output array with the float data type or not. Must be on to use non-integer spacing of voxels.
| dataType | string | Data type of the Numpy output array. Boolean is recommended to reduce the size of the output array, but if you'd like to handle collisions or debug them, must be set to integer or float. Can be any Numpy data type |
| useWarnings | bool | Whether or not to display warnings when generating output arrays.|
| useSpheres | bool | Whether or not to use spheres when rendering the output array. If false, boxes will be used instead.|
