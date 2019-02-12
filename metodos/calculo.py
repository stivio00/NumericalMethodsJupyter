#Libreria de funciones pra calculo numerico


def derivada(f, x, h=1e-6):
    return ( f(x+h) - f(x) ) / h

def derivada_i(f, x, h=1e-6):
    return ( f(x) - f(x-h) ) / h

def derivada_c(f, x, h=1e-6):
    h = h/2
    return ( f(x +h) - f(x-h) ) / (2*h)


def diff(f,x,i ,h=1e-6):
    "i=numero entero de 0,...,N-1(numero de columnas -1)"
    fx = f(x)
    x[i] = x[i] +h
    fxh = f(x)
    return (fxh-fx)/h

def jacn(f,x, h=1e-6):
    N = len(x) #Columnas
    M = len(f(x))
    
    J = np.zeros((N, M))
    for i in range(N):
        J[:,i] = diff(f,x,i,h)
    
    return J


def nr_multi(f,xi,jac, tol=1e-3, iter_max=1000):
    i = 0
    while abs(f(xi).dot(f(xi))) >= tol:
        i += 1 
        
        xi = xi - np.linalg.solve(jac(xi),f(xi))
        print("x(i+1)=" +str(xi))
        
    return 0