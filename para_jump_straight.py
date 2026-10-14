from numpy import exp
from scipy.integrate import quad

g = 9.81  # acceleration due to gravity in m/s^2
v_term = 54.0  # terminal velocity in m/s

def integrand(t):
    e_term = exp(-2*g*t/(v_term))
    return (1-e_term)/(1+e_term)

h = float(input("Enter starting height (in meters): "))
t = 0.0
v = 0.0
y = h

time = []
position = []
velocity = []

file = open("para_jump_straight_output.txt", "w")

while (y >= 0):

    t += 0.1
    y = h - v_term*quad(integrand, 0, t)[0]
    v = -v_term*integrand(t)
    time.append(t)
    position.append(y)
    velocity.append(v)
    file.write(f"{t:.1f} {y:.2f} {v:.2f}\n")
    if y <= 0:
        break

file.close()