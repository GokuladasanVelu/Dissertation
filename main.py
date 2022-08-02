import math
from AnimePlot import anim_plot
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

np = 100
npindex = np+1
spwise = 10
b = 2
gammao = 1
tmax = 0.5
dt = 1.25 * (10 ** (-3))
d = 0.02 # Smoothing factor
reynoldsnumber = math.inf
delT = 1
r = 0.15
coordinate_type = 3  # Symmetric line space
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

coordinates = vortex_coodinates(np, b, gammao, np, coordinate_type)
y = coordinates[0]
circulation = coordinates[1]
z = coordinates[2]
ploty = y
plotz = circulation
plt.title("Circulation Distribution")
plt.xlabel("Y-axis")
plt.ylabel("Circulation (" + "\u0393" + ")")
plt.plot(ploty, plotz)
plt.show()
anim_plot(r, reynoldsnumber, d, tmax, dt, np, y, z, circulation)



# rcore = coreradiusandvelocity b = plt.show()[0]
# # vcore = coreradiusandvelocity[1]
# # plt.plot(rcore, vcore)
# #
