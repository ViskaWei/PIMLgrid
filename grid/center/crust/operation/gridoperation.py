from abc import ABC, abstractmethod

from base.center.crust.baseoperation import BaseOperation,\
    BaseModelOperation, PolarScaleOperation

from ..data.constants import Constants
from ..data.basegrid import BaseGrid, StellarGrid
from .baseoperation import ApplyInterpOperation


#basegrid----------------------------------------------------------------------------------------------------------------------
class BaseGridOperation(BaseOperation):
    @abstractmethod
    def perform_on_Grid(self, Grid: BaseGrid) -> BaseGrid:
        pass

class BaseGridModelOperation(BaseGridOperation, BaseModelOperation):
    @abstractmethod
    def perform_on_Grid(self, Grid: BaseGrid) -> BaseGrid:
        self.model.apply_on_Grid(Grid)

class  CoordxifyGridOperation(PolarScaleOperation, BaseGridOperation):
    def perform_on_Grid(self, Grid: BaseGrid) -> BaseGrid:
        Grid.coordx = self.perform(Grid.coord)
        Grid.coordx_rng = Grid.coordx.max(0) - Grid.coordx.min(0)
        Grid.coordx_scaler = self.scaler
        Grid.coordx_rescaler = self.rescaler


class ScaleStellarGridOperation(BaseGridOperation):
    def perform(self, coord):
        origin = coord.min(0)
        OP = PolarScaleOperation(origin, Constants.PHYTICK)
        return OP.perform(coord)

    def perform_on_Grid(self, Grid: StellarGrid):
        if hasattr(Grid, "box"):
            origin = Grid.box["min"]
        else:
            origin = Grid.coord.min(0)

        OP = PolarScaleOperation(origin, Constants.PHYTICK)
        OP.perform_on_Grid(Grid)


