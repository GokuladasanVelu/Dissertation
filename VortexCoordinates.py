import numpy as np


def vortex_coodinates(npts):
    y = np.linspace(-1, 1, npts)
    z = np.zeros(npts)

    return y, z
