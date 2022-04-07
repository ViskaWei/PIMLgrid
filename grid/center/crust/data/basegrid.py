import numpy as np
import pandas as pd
from .constants import Constants

class BaseGrid(object):
    def __init__(self, coord, value) -> None:
        self.coord  = coord
        self.value  = value

class StellarGrid(BaseGrid):
    """ Base class for all spec grids. """
    def __init__(self, coord, value) -> None:
        super().__init__(coord, value)
        self.coordx = None
    
        self.PhyShort = Constants.PhyShort
        self.dfcoord = self.set_dfcoord()
    
    def set_dfcoord(self):
        return pd.DataFrame(self.coord, columns=self.PhyShort)

    def get_coord_idx(self, coord_i):
        return np.where(np.prod(self.coord == coord_i, 1))[0][0]        

    def get_coord_value(self, coord_i):
        idx = self.get_coord_idx(coord_i)
        return self.value[idx]
    