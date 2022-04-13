from base.center.crust.baseprocess import BaseProcess
from grid.center.crust.data.basegrid import BaseGrid, StellarGrid
from ..operation.gridoperation import BaseGridOperation,\
    StellarUnifyGridOperation, InterpBuilderGridOperation,\
    StellarBoxOperation


class StellarGridProcess(BaseProcess):
    def __init__(self) -> None:
        self.operation_list: list[BaseGridOperation] = None
    def set_process(self, PARAM, MODEL, DATA):
        self.operation_list = [
            StellarBoxOperation(PARAM["box_name"]),
            StellarUnifyGridOperation(),
            InterpBuilderGridOperation(MODEL["interp"]),
        ]
        
    def start(self, Grid: StellarGrid):
        for operation in self.operation_list:
            operation.perform_on_Grid(Grid)


