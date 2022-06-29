import math


def velocities(np, y, z, circulation):
    pi = math.pi
    npindex = np

#    u_list = []
#     u_value = 0
#     u_list.extend([u_value for i in range(1, npindex)])
    u_final = []

#    v_list = []
#     v_value = 0
#     v_list.extend([v_value for i in range(1, npindex)])
    v_final = []

#    w_list = []
#     w_value = 0
#     w_list.extend([w_value for i in range(1, npindex)])
    w_final = []

    for i in range(1, npindex):

        for j in range(1, npindex):
            if i is not j:
                r2 = (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2
                u = circulation * ((z[j] - z[i]) / r2 / 2 / pi)
                u_final.append(u)
                v = -circulation * ((y[j] - y[i]) / r2 / 2 / pi)
                v_final.append(v)
                w = u + v
                w_final.append(w)

    return v_final, u_final, w_final
