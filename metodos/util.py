import sys
import numpy as np
import matplotlib.pyplot as plt

def diag_fases(f,t=0, y1_lim=[-6,6], y2_lim=[-4,4],resolution=10):
    """ Funcion que grafica un diagrama de fases 
    si se pasa la funcion de transformación de estado f(t,y)
    donde t es la variable independiente y y el vector de estado. 
    Esta vrsion solo grafica transiciones de N=2 hacia M=2
    y se evalua en 
    
    """
    y1 = np.linspace(y1_lim[0],y1_lim[1], resolution)
    y2 = np.linspace(y2_lim[0],y2_lim[1], resolution)
    Y1, Y2 = np.meshgrid(y1, y2)
    u, v = np.zeros(Y1.shape), np.zeros(Y2.shape)
    NI, NJ = Y1.shape
    for i in range(NI):
        for j in range(NJ):
            x, y = Y1[i, j], Y2[i, j]
            yprime = f(t,[x, y])
            u[i,j], v[i,j] = yprime[0], yprime[1]
     
    plt.quiver(Y1, Y2, u, v, color='r')
    plt.streamplot(Y1, Y2, u, v, density=[resolution/10, resolution/10])
    plt.xlabel('$y_1$')
    plt.ylabel('$y_2$')
    plt.xlim(y1_lim)
    plt.ylim(y2_lim)
    plt.show()
    
    
    
def init_animation():
    pass

