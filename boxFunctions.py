import numpy as np

def structureLimits(atomCoords):
    ''' 
    Get the upper and lower bounds for every dimension from the given set of coordinates.
    Used to get the ranges of cartesian coordiantes that describe the entire structure.
    
    Output array is in the following format:
            x y z
        min . . .
        max . . .
        
    '''
    
    structureLimits=np.array([
        [np.min(atomCoords[:,dimension]) for dimension in range(0,3)], 
        [np.max(atomCoords[:,dimension]) for dimension in range(0,3)]],
        dtype=np.float32
    )
    
    return structureLimits

def samplePoints(structureLimits,spacing=1):
    '''
    Given boundaries, generate a set of sample points spaced at regular intervals.
    Currently, we round to the nearest integer.
    
    Default spacing interval is 1 angstrom
    
    '''
    
    if not isinstance(spacing, int):
        raise ValueError("sampleRate is not a integer value!")

    # Round min and max to the nearest integer
    # Add one (1) sample to the end to include end-point
    structureLimits[0]=np.floor(structureLimits[0])
    structureLimits[1]=np.ceil(structureLimits[1])+spacing
    
    # Generate an array of sample points for each dimension
    x_points=np.arange(structureLimits[0,0],structureLimits[1,0],spacing, dtype=int)
    y_points=np.arange(structureLimits[0,1],structureLimits[1,1],spacing, dtype=int)
    z_points=np.arange(structureLimits[0,2],structureLimits[1,2],spacing, dtype=int)

    ''' Use numpy.meshgrid to generate the sample points. Equivalent to the following:
    
    samplePoints=[]
    for x in x_points
        for y in y_points
            for z in z_points
                samplePoints.append([x,y,z])
    '''
    
    x,y,z=np.meshgrid(x_points, y_points, z_points, indexing='ij')
    samplePoints=np.column_stack((x, y, z))
    
    return samplePoints

def centralAA():
    # Function to find the central amino acids
    pass
        
def scanRange(origin,delta,size,voxel):
    scanRange=np.zeros((3,size),dtype=int)
    for dimension,component in enumerate(boxOrigin):
        # Add one (1) voxel to maximum to include endpoint
        scanMin,scanMax=component-delta,component+delta+voxel
        scanRange[dimension,:]=np.arange(scanMin,scanMax,voxel)
    return scanRange

def buildBox(boxOrigin, boxSize, voxel, atomCoords):
    # bitshift the boxsize (divide by 2) and store delta as integer value
    delta=np.intc(boxSize>>1)
    size=np.intc(boxSize/voxel+voxel)

    # Get our scanning range for the algorithm from the origin point
    # We want to avoid recomputing this range every iteration because it is constant
    scanMin=[component-delta for component in boxOrigin]
    scanMax=[component+delta+voxel for component in boxOrigin]

    foundAtoms=[]
    for index,atom in enumerate(atomCoords):
        if np.array_equal(atom,boxOrigin):
            continue # Exclude the central atom from atoms to search
        for dimension,component in enumerate(atom[:3]):
            if (component-scanMin[dimension])*(component-scanMax[dimension]) > 0:
                break # One dimension was out of range, so no need to check the rest
        else:
            # We have found an atom that is within the box
            foundAtoms.append(index)

    return foundAtoms
            