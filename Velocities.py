import math
# -------------------------Velocity-----------------------------------

def velocities(r, time, reynoldsnumber, np, y, z, circulation, d):
    pi = math.pi
    npindex = len(y)
    u = [0] * npindex
    v = [0] * npindex
    vthj = [0] * npindex



    # for i in range(0, npindex):
    #     for j in range(0, npindex):
    #         if i is not j:
    #             r2 = ((y[i] - y[j]) ** 2) + ((z[i] - z[j]) ** 2) + (d ** 2)
    #             u[j] = u[j] + (circulation[i] * (z[j] - z[i])) / (r2 * 2 * pi)
    #             v[j] = v[j] - ((circulation[i]) * (y[j] - y[i])) / (r2 * 2 * pi)

    for i in range(0, npindex):
        for j in range(0, npindex):
            if i is not j:
                r2 = ((y[i] - y[j]) ** 2) + ((z[i] - z[j]) ** 2) + (d ** 2)
                rcjo = ((y[i] - y[j]) ** 2)

    rcj = rcjo + 3.17 * ((time/reynoldsnumber) ** (1/2))
    rcj2 = rcj ** 2

    if rcj2 > r2:
        for i in range(0, npindex):
            for j in range(0, npindex):
                exp = math.exp(-1.25643 * (r / rcj) ** 2)
                vthj[j] = (circulation[j] / (2 * pi * r)) * (1-exp)
                th = math.atan2((y[j] - y[i]), (z[j] - z[j]))
                u[j] = -vthj[j] * math.sin(th)
                v[j] = vthj[j] * math.cos(th)
    else:
        for i in range(0, npindex):
            for j in range(0, npindex):
                u[j] = u[j] + (circulation[i] * (z[j] - z[i])) / (r2 * 2 * pi)
                v[j] = v[j] - ((circulation[i]) * (y[j] - y[i])) / (r2 * 2 * pi)

    return u, v
