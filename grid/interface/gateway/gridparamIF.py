from base.interface.gateway.baseparamIF import ParamIF
from grid.center.crust.data.constants import Constants


class GridParamIF(ParamIF):
    required_attribute = ["box_name"]

    def set_param(self, PARAM):
        self.box_name = self.get_arg('box_name', PARAM)

        self.interp = self.get_arg('interp', PARAM, "RBF")
        self.OBJECT_PATH = self.get_arg('OBJECTPATH', PARAM, Constants.BOSZ_PATH)

        self.set_param_dict()

    def set_param_dict(self):
        self.OBJECT = {"OBJECTPATH": self.OBJECT_PATH}

        self.MODEL  = {'interp': {'type': self.interp}}

        self.OP     = {'box_name': self.box_name}
