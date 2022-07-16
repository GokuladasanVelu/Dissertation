from Velocities import velocities
import matplotlib.pyplot as plt
# -----------Plotting particles------------


def anim_plot(d, tmax, dt, np, y, z, circulation):
    time = (tmax / dt) + 1
    time = int(time)
    yy = []
    zz = []
    for i in range(1, time):
        vel = velocities(np, y, z, circulation, d)
        u = [vel[0]]
        v = [vel[1]]
        u = u[(len(u) - 1)]
        v = v[(len(v) - 1)]
        for j in range(0, (len(y))):
            y[j] = y[j] + (u[j] * dt)
            z[j] = z[j] + (v[j] * dt)
        yy.append(y)
        zz.append(z)

    # final plot:
    plotz = zz[(len(zz) - 1)]
    ploty = yy[(len(yy) - 1)]

    plt.plot(ploty, plotz)
    a = plt.show()

    return a