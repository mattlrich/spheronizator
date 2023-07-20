import box_algorithm as box

# Use biopython to parse pdb files

# Testing input data
boxSize=20
channels=7
boxOrigin=[2,4,5]
atomCoords=[[1,1,1],[2,2,2],[3,3,3],[4,4,4],[100,100,100],[2.5,2.5,2.5],[2,4,5]]
atomNames=[12,14,32]

# Function expects the following data in this order:
# boxSize, boxOrigin, atomCoords, atomNames, pqr, sasa, voxel, channels
box.buildBox(boxSize,boxOrigin,atomCoords,atomNames,1,1,1,1)
