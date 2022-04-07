
from abc import ABC, abstractmethod
from base.center.crust.basemodel import BaseModel, RBFInterpBuilderModel
from grid.center.crust.data.basegrid import BaseGrid
from grid.interface.gateway.gridstorerIF import InterpStorerIF


class BaseInterpBuilderGridModel(BaseModel):
    @abstractmethod
    def apply_on_Grid(self, Grid: BaseGrid) -> None:
        pass
    @abstractmethod
    def store(self, DATA_DIR, name="interp"):
        pass

class RBFInterpBuilderGridModel(RBFInterpBuilderModel):
    def apply_on_Grid(self, Grid: BaseGrid) -> None:
        interpolator = self.apply(Grid.coordx, Grid.value)
        Grid.interpolator = interpolator
        Grid.builder = self.builder


        

