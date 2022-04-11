from abc import ABC, abstractmethod
from base.center.crust.basemodel import BaseModel, RBFInterpBuilderModel
from grid.center.crust.data.basegrid import BaseGrid, StellarGrid


class BaseInterpBuilderGridModel(BaseModel):
    @abstractmethod
    def apply_on_Grid(self, Grid: BaseGrid) -> None:
        pass
    @abstractmethod
    def store(self, DATA_DIR, name="interp"):
        pass

class RBFInterpBuilderGridModel(RBFInterpBuilderModel):
    def apply_on_Grid(self, Grid: StellarGrid) -> None:
        interpolator = self.apply(Grid.unit_coord, Grid.value)
        def unit_coord_interpolator(eval_coord, scale=True):
            unit_coord = Grid.unify(eval_coord) if scale else eval_coord
            return interpolator(unit_coord)   
        Grid.interpolator = unit_coord_interpolator
        Grid.builder = self.builder


        

