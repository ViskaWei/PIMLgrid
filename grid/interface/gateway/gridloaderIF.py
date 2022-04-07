from base.interface.gateway.baseloaderIF import DictLoaderIF, ObjectLoaderIF
from grid.center.crust.data.basegrid import StellarGrid


class StellarGridLoaderIF(ObjectLoaderIF):
    """ class for loading Spec Grid (wave, flux, Physical Param for each flux..). """
    def set_param(self, PARAM):
        self.loader = DictLoaderIF(PARAM["PATH"])

    def load(self):
        coord = self.loader.load_arg("para")
        value = self.loader.load_arg("flux")
        return StellarGrid(coord, value)
        

