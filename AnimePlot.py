from Velocities import velocities
import matplotlib.pyplot as plt
# -----------Plotting particles------------

def anim_plot(r, reynoldsnumber, d, tmax, dt, np, y, z, circulation):
    time = (tmax / dt) + 1
    time = int(time)
    yy = []
    zz = []
    umat = []
    vmat = []
    yy.append(y)
    zz.append(z)
    for i in range(1, time):
        vel = velocities(r, dt, reynoldsnumber, np, yy[(len(yy)-1)], zz[(len(zz)-1)], circulation, d)
        u = [vel[0]]
        v = [vel[1]]
        u = u[(len(u) - 1)]
        v = v[(len(v) - 1)]
        umat.append(u)
        vmat.append(v)
        aa = []
        bb = []
        for j in range(0, (len(y))):
            a = y[j] + (u[j] * dt)
            b = z[j] + (v[j] * dt)
            aa.append(a)
            bb.append(b)
        yy.append(aa)
        zz.append(bb)
        y = yy[(len(yy)-1)]
        z = zz[(len(zz)-1)]


    # final plot:
    # plotz = zz[(len(zz) - 1)]
    # ploty = yy[(len(yy) - 1)]
    #
    # plt.plot(ploty, plotz)
    # a = plt.show()
    #
    # return a
    for j in range(0, len(yy)):
        plt.clf()
        ploty = yy[j]
        plotz = zz[j]
        plt.plot(ploty, plotz)
        plt.pause(0.01)
    plt.show()


