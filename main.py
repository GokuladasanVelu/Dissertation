from Plot import plot
from Velocities import velocities
from VortexCoordinates import vortex_coodinates
import matplotlib.pyplot as plt
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
from VortexCoreradius_velocity import vortexcoreradius_velocity

np = 50
npindex = np+1
spwise = 10
b = 2
gammao = 1.4
tmax = 2
dt = 0.01
d = 0.05 #Smoothing factor
reynoldsnumber = 40
delT = 1
rcjo = 12
r = 1
# -------------------------Coordinates Manual entry-------
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
plot(d, tmax, dt, np, y, z, circulation)
coreradiusandvelocity = vortexcoreradius_velocity(np, rcjo, reynoldsnumber, delT, circulation, r)
rcore = coreradiusandvelocity[0]
vcore = coreradiusandvelocity[1]
plt.plot(rcore, vcore)
b = plt.show()