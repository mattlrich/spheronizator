import boxFunctions
import numpy as np

class proteinBox:

    def __init__(self,atoms):

        # Input should be a list of Biopython atom objects and they should have their records updated with the corresponding mol2 file
        self.atoms=atoms

    def buildData(self):
        pass

    def _extract_coords(self):
        
        self.centralCoords=[]
        self.atomCoords=[]

        for atom in self.atoms:
            if atom.isAA: 
                if atom.isCentral:
                    self.centralCoords.append(atom.get_coord())

                self.atomCoords.append(atom.get_coord())

        self.centralCoords=np.array(self.centralCoords, dtype=np.float32)
        self.atomCoords=np.array(self.atomCoords, dtype=np.float32)





