import numpy as np
import matplotlib.pyplot as plt

from grid.center.crust.data.constants import Constants
from grid.center.crust.data.basegrid import StellarGrid


def eval_interpolator(Object: StellarGrid, axis = 1):
    pmt0 = Object.box["mid"]
    pmt2 = np.copy(pmt0)
    pmt2[axis] += Constants.PHYTICK[axis]
    pmt1 = 0.5 * (pmt0 + pmt2)

    flux0 = Object.get_coord_value(pmt0)
    flux2 = Object.get_coord_value(pmt2)
    flux1 = Object.interpolator(pmt1)

    wave = np.arange(len(flux0))
    plt.plot(wave, flux0, label= pmt0, c='b')
    plt.plot(wave, flux1, label = pmt1, c='r')
    plt.plot(wave, flux2, label = pmt2, c='cyan')
    plt.legend()