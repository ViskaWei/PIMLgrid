from base.interface.gateway.baseprocessIF import ProcessIF
from grid.center.crust.data.basegrid import StellarGrid
from grid.center.crust.process.gridprocess import StellarGridProcess
from .gridloaderIF import StellarGridLoaderIF

class StellarGridProcessIF(ProcessIF):
    def __init__(self) -> None:
        super().__init__()
        self.Loader   = StellarGridLoaderIF()
        self.Process  = StellarGridProcess()
        self.Storer   = None

    def set_data(self, DATA_PARAM):
        pass

    def set_param(self, OP_PARAM):
        self.OP_PARAM = self.paramIF(OP_PARAM)
    
    def set_model(self, MODEL_PARAM):
        self.OP_MODEL = MODEL_PARAM

    def paramIF(self, PARAMS):
        #TODO create class later
        return PARAMS

    def interact_on_Object(self, Grid: StellarGrid):
        super().interact_on_Object(Grid)
