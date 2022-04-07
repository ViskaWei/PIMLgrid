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




