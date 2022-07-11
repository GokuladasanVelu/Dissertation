def vortexcoreradius(np, rcjo, reynoldsnumber, delT):
    rc = 0
    coreradius=[]
    for i in range(0, np):
        inversereynoldsnumber = 1 / reynoldsnumber
        rc = rcjo + 3.17 * (delT * inversereynoldsnumber) ** (1 / 2)
        coreradius.append(rc)
    return rc
