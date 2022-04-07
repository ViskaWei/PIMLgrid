from base.center.crust.baseprocess import BaseProcess
from ..data.basegrid import StellarGrid
from ..operation.boxoperation import BaseBoxOperation, StellarBoxOperation


class StellarBoxProcess(BaseProcess):
    def __init__(self) -> None:
        self.operation_list: list[BaseBoxOperation] = None
    
    def set_process(self, PARAM, MODEL, DATA):
        self.operation_list = [
            StellarBoxOperation(PARAM["box_name"]),
        ]   
    def start(self, Grid: StellarGrid):
        for operation in self.operation_list:
            operation.perform_on_Box(Grid)
