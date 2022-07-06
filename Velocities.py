import math
# -------------------------Velocity-----------------------------------
#

def velocities(np, y, z, circulation, d):
    pi = math.pi
    npindex = len(y)
    u = [0] * npindex
    v = [0] * npindex
    # w_final = []
    # dict_w = {}

    for i in range(0, npindex):

        for j in range(0, npindex):
            if i is not j:
                r2 = ((y[i] - y[j]) ** 2) + ((z[i] - z[j]) ** 2) + (d ** 2)
                u[j] = u[j] + (circulation[i] * (z[j] - z[i])) / (r2 * 2 * pi)
                v[j] = v[j] - ((circulation[i]) * (y[j] - y[i])) / (r2 * 2 * pi)
                w = u + v
                # w_final.append(w)

    return u, v
