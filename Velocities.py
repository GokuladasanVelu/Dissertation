import math


def velocities(np, y, z, circulation):
    pi = math.pi
    npindex = np+1

    u_list = []
    u_value = 0
    u_list.extend([u_value for i in range(1, npindex)])

    v_list = []
    v_value = 0
    v_list.extend([v_value for i in range(1, npindex)])

    w_list = []
    w_value = 0
    w_list.extend([w_value for i in range(1, npindex)])

    for i in range(1, npindex):

        for j in range(1, npindex):
            r2 = (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2
            u_list[j] = u_list[j] + circulation * (z[j] - z[i])/r2/2/pi
            v_list[j] = v_list[j] - circulation * (z[j] - z[i])/r2/2/pi
            w_list = u_list[j] + v_list[j]

    return v_list, u_list, w_list
