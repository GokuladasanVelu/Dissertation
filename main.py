import math
from AnimePlot import anim_plot
from GUI import GUI
from VortexCoordinates import vortex_coodinates
import matplotlib.pyplot as plt

GUI()
np = 100
b = 2
gammao = 1
tmax = 2
dt = 0.01
d = 0.1  # Smoothing factor

npindex = np+1
reynoldsnumber = math.inf
delT = 1
r = 0.15
coordinate_type = 1  # Symmetric line space
h = 0.1
coordinates = vortex_coodinates(np, b, gammao, np, coordinate_type)
y = coordinates[0]
circulation = coordinates[1]
z = coordinates[2]
ploty = y
plotz = circulation
plt.title("Circulation Distribution")
plt.xlabel("Y-axis")
plt.ylabel("Circulation G(y)")
plt.plot(ploty, plotz)
plt.show()
anim_plot(r, reynoldsnumber, d, tmax, dt, np, y, z, circulation, h)
