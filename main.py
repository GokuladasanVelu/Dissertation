from LagrangianCirculation import lagrangian_circulation
from Velocities import velocities
from VortexCoordinates import vortex_coodinates
# %% initial list of points
# %% number of points
x = input("Number of point vortices: ")
np = int(x)
spanwise = input("Distance in span wise direction: ")
y = int(spanwise)

span = input("Span: ")
b = int(span)
a=1
maxcirculation = input("Maximum circulation: ")
gammao = int(maxcirculation)
circulation = lagrangian_circulation(y, b, gammao)
npindex=np+1
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

coordinates = vortex_coodinates(np)

