import math

# -------------------------Velocity-----------------------------------


def velocities(np, y, z, circulation):
    pi = math.pi
    npindex = np
    u_final = []
    v_final = []
    w_final = []
    dict_w = {}
    dict_u = {}
    dict_v = {}

    for i in range(0, npindex):

        for j in range(0, npindex):
            if i is not j:
                r2 = (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2
                u = (circulation[j] * (z[j] - z[i])) / (r2 / 2 / pi)
                u_final.append(u)
                v = (-(circulation[j]) * (y[j] - y[i])) / (r2 / 2 / pi)
                v_final.append(v)
                w = u + v
                w_final.append(w)
                # Dictionary for key pair of vortex numbers and their respective w_final
                k = [i, j]
                k1 = str(k)
                dict_w[k1] = w
                dict_u[k1] = u
                dict_v[k1] = v

    return u_final, v_final, w_final, dict_u, dict_v, dict_w


