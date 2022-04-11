from base.interface.gateway.baseprocessIF import ProcessIF
from grid.center.crust.data.basegrid import StellarGrid
from grid.center.crust.process.gridprocess import StellarGridProcess
from .gridloaderIF import StellarGridLoaderIF
from .gridparamIF  import StellarGridParamIF

class StellarGridProcessIF(ProcessIF):
    def __init__(self) -> None:
        super().__init__()
        self.Loader  = StellarGridLoaderIF()
        self.Param   = StellarGridParamIF()
        self.Process = StellarGridProcess()
        self.Storer  = None

    def interact_on_Object(self, Grid:StellarGrid) -> None:
        super().interact_on_Object(Grid)
