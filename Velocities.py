import math
# -------------------------Velocity-----------------------------------


def velocities(r, dt, reynoldsnumber, np, y, z, circulation, d):
    pi = math.pi
    npindex = len(y)
    u = [0] * npindex
    v = [0] * npindex
    vthj = [0] * npindex
    inversereynolds = 1/reynoldsnumber

    for i in range(0, npindex):
        for j in range(0, npindex):
            if i is not j:
                r2 = ((y[i] - y[j]) ** 2) + ((z[i] - z[j]) ** 2) + (d ** 2)
                u[j] = u[j] + (circulation[i] * (z[j] - z[i])) / (r2 * 2 * pi)
                v[j] = v[j] - ((circulation[i]) * (y[j] - y[i])) / (r2 * 2 * pi)

    # core Radius
    # rcjo = (y[1] - y[0])
    # for i in range(0, npindex):
    #     for j in range(0, npindex):
    #         if i is not j:
    #             r2 = ((y[i] - y[j]) ** 2) + ((z[i] - z[j]) ** 2) + (d ** 2)
    #             rcj = rcjo + 3.17 * ((dt * inversereynolds) ** (1 / 2))
    #             rcj2 = (rcj ** 2) + (d ** 2)
    #             if rcj2 > r2:
    #                 exp = math.exp(-1.25643 * (r / rcj) ** 2)
    #                 vthj[j] = (circulation[j] / (2 * pi * r)) * (1 - exp)
    #                 th = math.atan2((y[i] - y[j]), (z[i] - z[j]))
    #                 u[j] = u[j] - vthj[j] * math.sin(th)
    #                 v[j] = v[j] + vthj[j] * math.cos(th)
    #             else:
    #                 r2 = ((y[i] - y[j]) ** 2) + ((z[i] - z[j]) ** 2) + (d ** 2)
    #                 u[j] = u[j] + (circulation[i] * (z[j] - z[i])) / (r2 * 2 * pi)
    #                 v[j] = v[j] - ((circulation[i]) * (y[j] - y[i])) / (r2 * 2 * pi)

    return u, v
