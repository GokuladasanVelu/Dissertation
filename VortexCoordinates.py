import numpy as npy
from LagrangianCirculation import lagrangian_circulation


def vortex_coodinates(npts, b, gammao, np):
    z = b/2
    y0 = npy.linspace(0, z, npts)
    dy = y0[1]-y0[0]

    # place point vortex at three quarter point
    y = y0 + (0.75*dy)
    y = list(y)
    y.pop(np-1)

    # Generate negative side of wake
    circulation = lagrangian_circulation(y, b, gammao, npts, dy)
    flippedy = -npy.flipud(y)
    flippedy = list(flippedy)
    flipped_circulation = -npy.flipud(circulation)
    flipped_circulation = list(flipped_circulation)
    withnegativey = flippedy + y
    withnegative_circulation = flipped_circulation + circulation
    lengthy = len(withnegativey)
    z = npy.zeros(lengthy)

    return withnegativey, withnegative_circulation, z
