import numpy as npy

from LagrangianCirculation import lagrangian_circulation
from Velocities import velocities
from VortexCoordinates import vortex_coodinates
import matplotlib.pyplot as plt
import numpy as npy
# %% initial list of points
# %% number of points

# --------------------x,b,np,gammao-------------------
# x = input("Number of point vortices: ")
# np = int(x)
# spanwise = input("Distance in span wise direction: ")
# spwise = int(spanwise)
# span = input("Span: ")
# b = int(span)
# maxcirculation = input("Maximum circulation: ")
# gammao = int(maxcirculation)
# npindex=np+1
# -------------------------------------------------------

np = 32
npindex = np+1
spwise = 10
b = 2
gammao = 1
tmax = 2
dt = 0.1
d = 0.1
# -------------------------Coordinates Manual entry---------------------
# npaslist=[]
# finalcoordinates=[]
#
# for i in range (1, npindex):
#     npaslist.append(i)
#
# for i in npaslist:
#     if np > 0:
#         j = str(i)
#         a = VortexCoordinates()
#         a.y = input("Y coordinate of "+"vortex number "+j+":")
#         a.z = input("Z coordinate of "+"vortex number "+j+":")
#         l = [a.x, a.y]
#         finalcoordinates.append(l)
#     else:
#         print("no vortices present")
# -------------------------------------------------------------------------

coordinates = vortex_coodinates(np, b, gammao, np)
y = coordinates[0]
circulation = coordinates[1]
z = coordinates[2]
time = (tmax/dt)+1
time = int(time)
yy = []
zz = []
for i in range(1, time):
    vel = velocities(np, y, z, circulation, d)
    u = [vel[0]]
    v = [vel[1]]
    u = u[(len(u)-1)]
    v = v[(len(v)-1)]
    for i in range(0, (len(y))):
        y[i] = y[i] + (u[i]*dt)
        z[i] = z[i] + (v[i]*dt)
    yy.append(y)
    zz.append(z)

# final plot:
plotz =zz[(len(zz)-1)]
ploty =yy[(len(yy)-1)]

plt.plot(ploty, plotz)
plt.show()










