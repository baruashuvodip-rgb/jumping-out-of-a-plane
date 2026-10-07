from scipy.integrate import quad
from math import exp

g = 9.81  # acceleration due to gravity in m/s^2
v_t = 54 # terminal velocity in m/s

def integrand(t):
    e_term = exp(-2*g*t/(v_t))
    return (1-e_term)/(1+e_term)

h = float(input("Enter starting height (in meters): "))

file = open("para_jump_output.txt", "w")
t = 0.0

falling = True
while (falling == True):
    
    y_t = h - v_t*quad(integrand, 0, t, points=4)[0]
    if y_t < 0:
        y_t = 0
    file.write(f"{t}, {y_t}\n")

    if y_t == 0:
        falling = False
    else:
        t += 0.1  # Increment time by 0.1 seconds

file.close()
