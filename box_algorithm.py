import numpy as np

def buildBox(boxSize, boxOrigin, atomCoords, atomNames, pqr, sasa, voxel, channels):
    # bitshift the boxsize (divide by 2) and store delta as integer value
    delta=np.intc(boxSize>>1)
    size=np.intc(boxSize/voxel+voxel)

    # Get our scanning range for the algorithm from the origin point
    # We want to avoid recomputing this range every iteration because it is constant
    scanRange=np.zeros((3,size),dtype=int)
    for dimension,component in enumerate(boxOrigin):
        # Add one (1) voxel to maximum to include endpoint
        scanMin,scanMax=component-delta,component+delta+voxel
        scanRange[dimension,:]=np.arange(scanMin,scanMax,voxel)

    scanMin=[component-delta for component in boxOrigin]
    scanMax=[component+delta+voxel for component in boxOrigin]
          
    for index,atom in enumerate(atomCoords):
        for dimension,component in enumerate(atom[:3]):
            if (component-scanMin[dimension])*(component-scanMax[dimension]) > 0:
                break
        else:
            # We have found an atom that is within the box
            print("I've found an atom!", index)
            

def atomBox():
    print("Nothing here!")