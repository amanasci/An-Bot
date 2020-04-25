import matplotlib.pyplot as plt 
import numpy as np
from mpl_toolkits import mplot3d 
from numpy.lib.function_base import meshgrid
from mpl_toolkits.mplot3d.axes3d import Axes3D


def plot(y):
    
    """
        plot helps to plot the graph of a function defined as y(x).

        It accepts:
        > arg (String): It's the function y(x), written in variable x.
            Example: plot(x**2)

        > While writing equations one can use all numpy libraries, with numpy as np.
            Expample: plot(np.sin(x))

        

    """
    x=np.array(range(-100,100))
    z=eval(y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x,z)
    plt.savefig("An\\plot.png") 
    plt.close()

def plot3D(a):
    b = np.array(range(-100,100))
    c = np.array(range(-100,100))
    B,C = meshgrid(b,c)
    d=eval(a)  
    d=np.expand_dims(d,axis=0)

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(B,C,d, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
    plt.xlabel('b')
    plt.ylabel('c')
    plt.savefig("An\\plot3D.png")
    plt.close()
