import math
from tkinter import *
from tkinter import ttk
from AnimePlot import anim_plot
from VortexCoordinates import vortex_coodinates
import matplotlib.pyplot as plt
window = Tk()
window.title("Discrete Vortex Simulation")
window.geometry('350x500')
var = IntVar()


def get_value():
    a1_text = int(a1.get())
    b1_text = int(b1.get())
    c1_text = int(c1.get())
    d1_text = int(d1.get())
    e1_text = float(e1.get())
    f1_text = float(f1.get())
    getting = [a1_text, b1_text, c1_text, d1_text, e1_text, f1_text]
    config_selected = int(var.get())
    np = getting[2]
    b = getting[0]
    gammao = getting[1]
    tmax = getting[3]
    dt = getting[4]
    d = getting[5]  # Smoothing factor

    npindex = np + 1
    reynoldsnumber = math.inf
    delT = 1
    r = 0.15
    coordinate_type = 1  # Symmetric line space
    h = 0.1
    coordinates = vortex_coodinates(np, b, gammao, np, coordinate_type, config_selected)
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


a = Label(window, text="Wingspan (b)", font=("Helvetica", 11), justify=LEFT, anchor="w")
a.grid(sticky=W, row=1,column=0)
b = Label(window, text="Maximum Circulation (\u0393)", font=("Helvetica", 11), justify=LEFT, anchor="w").grid(sticky=W, row=3, column=0)
c = Label(window, text="Number of points (N)", font=("Helvetica", 11), justify=LEFT, anchor="w").grid(sticky=W, row=5, column=0)
d = Label(window, text="Total time (T)", font=("Helvetica", 11), justify=LEFT, anchor="w").grid(sticky=W, row=7, column=0)
e = Label(window, text="Time Step (\u03B4 t)", font=("Helvetica", 11), justify=LEFT, anchor="w").grid(sticky=W, row=9, column=0)
f = Label(window, text="Smoothing factor (\u03B4)", font=("Helvetica", 11), justify=LEFT, anchor="w").grid(sticky=W, row=11, column=0)
g = Label(window, text="Configuration", font=("Helvetica", 11), justify=LEFT, anchor="w").grid(sticky=W, row=13, column=0)

a1 = Entry(window)
a1.grid(row=1, column=1, padx=10, pady=20)
b1 = Entry(window)
b1.grid(row=3, column=1, padx=10, pady=20)
c1 = Entry(window)
c1.grid(row=5, column=1, padx=10, pady=20)
d1 = Entry(window)
d1.grid(row=7, column=1, padx=10, pady=20)
e1 = Entry(window)
e1.grid(row=9, column=1, padx=10, pady=20)
f1 = Entry(window)
f1.grid(row=11, column=1, padx=10, pady=20)
R1 = Radiobutton(text="Elliptic Loading", font=("Helvetica", 11), justify=LEFT, anchor="w", variable=var, value=1)
R1.grid(sticky=W, row=13, column=1)
R2 = Radiobutton(text="Fuselage/ Flap wing", font=("Helvetica", 11), justify=LEFT, anchor="w", variable=var, value=2)
R2.grid(sticky=W, row=14, column=1)
btn = ttk.Button(window, text="Run", command=get_value)
btn.grid(row=17, column=1, padx=10, pady=20)
# btn.pack()


window.mainloop()