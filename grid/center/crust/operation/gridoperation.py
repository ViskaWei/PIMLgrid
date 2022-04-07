import numpy as np
from abc import ABC, abstractmethod

from base.center.crust.baseoperation import BaseOperation,\
    BaseModelOperation, BuildScalerOperation

from ..data.constants import Constants
from ..data.basegrid import BaseGrid, StellarGrid
from ..model.interpmodel import BaseInterpBuilderGridModel, RBFInterpBuilderGridModel

#basegrid----------------------------------------------------------------------------------------------------------------------
class BaseGridOperation(BaseOperation):
    @abstractmethod
    def perform_on_Grid(self, Grid: BaseGrid) -> BaseGrid:
        pass

class BaseGridModelOperation(BaseGridOperation, BaseModelOperation):
    def perform_on_Grid(self, Grid: BaseGrid) -> BaseGrid:
        self.model.apply_on_Grid(Grid)

class CoordxGridOperation(BuildScalerOperation, BaseGridOperation):
    def perform_on_Grid(self, Grid: BaseGrid) -> BaseGrid:
        Grid.coordx = self.perform(Grid.coord)
        Grid.coordx_rng = Grid.coordx.max(0) - Grid.coordx.min(0)
        Grid.coord2idx = self.scaler
        Grid.idx2coord = self.rescaler

class StellarCoordxGridOperation(BaseGridOperation):
    def perform(self, coord):
        origin = coord.min(0)
        OP = CoordxGridOperation(origin, Constants.PHYTICK)
        return OP.perform(coord)

    def perform_on_Grid(self, Grid: StellarGrid):
        origin = Grid.box["min"] if hasattr(Grid, "box") else Grid.coord.min(0)
        OP = CoordxGridOperation(origin, Constants.PHYTICK)
        OP.perform_on_Grid(Grid)

class InterpBuilderGridOperation(BaseGridModelOperation):
    def set_model(self, model_type: str) -> BaseInterpBuilderGridModel:
        if model_type == "RBF":
            model = RBFInterpBuilderGridModel()
        elif model_type == "PCARBF":
            #TODO implement PCARBF
            pass
        else:
            raise ValueError("Unknown Interp model type: {}".format(model_type))
        return model

class StellarBoxOperation(BaseGridOperation):
    def __init__(self, box_name: Constants.DRs.keys()) -> None:
        self.name = box_name
        self.box = {"name": box_name}

    def perform(self, dfcoord=None):
        self.set_box_bnd()
        if dfcoord is not None: 
            self.is_coord_inbox(dfcoord)
        return self.box

    def perform_on_Grid(self, Grid: StellarGrid) -> StellarGrid:
        Grid.box = self.perform(Grid.dfcoord)

    def set_box_bnd(self):
        box_min, box_max, box_rng, box_num, box_mid = self.get_box_bnd(self.name)
        self.box["min"] = box_min
        self.box["max"] = box_max
        self.box["rng"] = box_rng
        self.box["num"] = box_num
        self.box["mid"] = box_mid

    def get_box_bnd(self, box_name):
        bnd = np.array(Constants.DRs[box_name])
        box_min, box_max = bnd.T
        box_rng = np.diff(bnd).T[0]
        box_num = box_rng / Constants.PHYTICK 
        box_mid = (box_num //2) * Constants.PHYTICK + box_min
        return box_min, box_max, box_rng, box_num, box_mid
    
    def is_coord_inbox(self, dfcoord):
        assert (dfcoord.min().values >= self.box["min"]).all() 
        assert (dfcoord.max().values <= self.box["max"]).all()