from tkinter import *
from tkinter import ttk

def GUI():
    window = Tk()
    window.title("Discrete Vortex Simulation")
    window.geometry('350x500')
    var = IntVar()
    a = Label(window, text="Wingspan (b)", font=("Helvetica", 11), justify=LEFT, anchor="w").grid(sticky=W, row=1,column=0)
    b = Label(window, text="Maximum Circulation (\u0393)", font=("Helvetica", 11), justify=LEFT, anchor="w").grid(sticky=W, row=3, column=0)
    c = Label(window, text="Number of points (N)", font=("Helvetica", 11), justify=LEFT, anchor="w").grid(sticky=W, row=5, column=0)
    d = Label(window, text="Total time (T)", font=("Helvetica", 11), justify=LEFT, anchor="w").grid(sticky=W, row=7, column=0)
    e = Label(window, text="Time Step (\u03B4 t)", font=("Helvetica", 11), justify=LEFT, anchor="w").grid(sticky=W, row=9, column=0)
    f = Label(window, text="Smoothing factor (\u03B4)", font=("Helvetica", 11), justify=LEFT, anchor="w").grid(sticky=W, row=11, column=0)
    g = Label(window, text="Configuration", font=("Helvetica", 11), justify=LEFT, anchor="w").grid(sticky=W, row=13, column=0)
    a1 = Entry(window).grid(row=1, column=1, padx=10, pady=20)
    b1 = Entry(window).grid(row=3, column=1, padx=10, pady=20)
    c1 = Entry(window).grid(row=5, column=1, padx=10, pady=20)
    d1 = Entry(window).grid(row=7, column=1, padx=10, pady=20)
    e1 = Entry(window).grid(row=9, column=1, padx=10, pady=20)
    f1 = Entry(window).grid(row=11, column=1, padx=10, pady=20)
    R1 = Radiobutton(text="Elliptic Loading", font=("Helvetica", 11), justify=LEFT, anchor="w", variable=var, value=1).grid(sticky=W, row=13, column=1)
    R2 = Radiobutton(text="Fuselage/ Flap wing", font=("Helvetica", 11), justify=LEFT, anchor="w", variable=var, value=2).grid(sticky=W, row=14, column=1)

    btn = ttk.Button(window, text="Run").grid(row=17, column=1, padx=10, pady=20)
    # btn.pack(side=ttk.RIGHT)
    window.mainloop()
