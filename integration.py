import numpy as np
from scipy.special import roots_legendre

def rectangularQuad_left(f, a, b, dx):
    N = int((b-a)/dx)
    result = 0.0
    for i in range(0,N+1,1):
        x = a + i*dx
        result += f(x)*dx
    return result

def rectangularQuad_right(f, a, b, dx):
    N = int((b-a)/dx)
    result = 0.0
    for i in range(0,N,1):
        x = a + (i+1)*dx
        result += f(x)*dx
    return result

def rectangularQuad_center(f, a, b, dx):
    N = int((b-a)/dx)
    result = 0.0
    for i in range(0,N,1):
        x = a + dx/2 + i*dx
        result += f(x)*dx
    return result

def trapezoidalQuad(f, a, b, dx):
    N = int((b-a)/dx) + 1
    w = np.full(N, 1.0)
    w[0] = w[N- 1] = 0.5
    x = np.linspace(a, b, len(w)) # Ensures that w and x have same length
    dx = x[1]- x[0] # Handles rounding weirdness
    y = w*f(x)
    return np.sum(y)*dx # Multiply here to avoid subtractive cancellation

def simpsonsQuad(f, a, b, dx):
    
    N = int((b-a)/dx) + 1
    
    if (N % 2 == 0): 
        N += 1 # Check if N is even, make odd if needed
    
    w = np.zeros(N) # Array of N elements, all set to zero
    
    # Use array slicing to set the values of our weight array
    w[::2] = 2.0
    w[1::2] = 4.0
    
    w[0] = w[N-1] = 1.0 # Set first and last values
    
    x = np.linspace(a, b, len(w)) # Compute evaluation points
    dx = x[1]- x[0] # Compute spacing since might be different
    
    y = w*f(x)/3.0
    
    return np.sum(y)*dx

def gaussianQuad(f, a, b, n):
    x, w = roots_legendre(n)
    y = w*f(((b-a)/2.0)*x + (b+a)/2.0)
    return np.sum(y)*(b-a)/2.0