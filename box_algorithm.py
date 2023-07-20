import numpy as np

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
            