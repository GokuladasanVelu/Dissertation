import math
# -------------------------Velocity-----------------------------------

def velocities(reynoldsnumber, np, y, z, circulation, d):
    pi = math.pi
    npindex = len(y)
    u = [0] * npindex
    v = [0] * npindex
    # w_final = []
    # dict_w = {}


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
                rcjo = (y[i] - y[j])
    if (rcjo ** 2) > r2:
        for i in range(0, npindex):
            for j in range(0, npindex):

    else:
        for i in range(0, npindex):
            for j in range(0, npindex):
                u[j] = u[j] + (circulation[i] * (z[j] - z[i])) / (r2 * 2 * pi)
                v[j] = v[j] - ((circulation[i]) * (y[j] - y[i])) / (r2 * 2 * pi)




    return u, v
