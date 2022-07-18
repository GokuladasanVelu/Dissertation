import math as mt


def vortexcoreradius_velocity(rcjo, reynoldsnumber, delT, circulation, r):
    pi = mt.pi
    coreradius=[]
    corevelocity=[]
    index = len(circulation)
    for i in range(0, index):
        delT = delT+1
        inversereynoldsnumber = 1 / reynoldsnumber
        rc = rcjo + 3.17 * (delT * inversereynoldsnumber) ** (1 / 2)
        coreradius.append(rc)

    for i in range(0, index):
        exp = mt.exp(-1.25643 * (r/coreradius[i])**2)
        vtheta = (circulation[i] / (2*pi*r)) * (1-exp)
        corevelocity.append(vtheta)

    return coreradius, corevelocity
