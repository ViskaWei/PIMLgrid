from abc import ABC, abstractmethod
from base.center.crust.baseoperation import BaseOperation, BaseModelOperation
from ..model.interpmodel import InterpBuilderModel, RBFInterpBuilderModel

from ..data.basegrid import BaseGrid

class ApplyInterpOperation(BaseOperation):
    def __init__(self, interpolator, rescaler=None) -> None:
        self.interpolator = interpolator
        self.rescaler = rescaler

    def perform(self, data):
        coordx = data if self.rescaler is None else self.rescaler(data)
        return self.interpolator(coordx)

class BaseBoxOperation(BaseOperation):

    def perform(self, dfcoord=None):
        self.set_box_bnd()
        if dfcoord is not None: 
            self.is_coord_inbox(dfcoord)
        return self.box

    @abstractmethod
    def set_box_bnd(self):
        pass

class InterpGridOperation(BaseModelOperation):
    def set_model(self, model_type: str) -> InterpBuilderModel:
        if model_type == "RBF":
            model = RBFInterpBuilderModel()
        elif model_type == "PCARBF":
            #TODO implement PCARBF
            pass
        else:
            raise ValueError("Unknown Interp model type: {}".format(model_type))
        return model



