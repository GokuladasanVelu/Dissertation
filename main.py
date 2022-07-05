from LagrangianCirculation import lagrangian_circulation
from Velocities import velocities
from VortexCoordinates import vortex_coodinates
from matplotlib import pyplot
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

vel = velocities(np, y, z, circulation)
u = []
for i in range(np):
    u.append(i)

v = circulation
pyplot.scatter(u, v)
pyplot.show()
