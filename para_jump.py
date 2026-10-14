from scipy.integrate import quad
from math import exp

g = 9.81  # acceleration due to gravity in m/s^2
v_t_initial = 54.0 #initial terminal velocity in m/s
v_t_parachute = 7.6 #terminal velocity with parachute in m/s

def integrand(t):
    e_term = exp(-2*g*t/(v_t))
    return (1-e_term)/(1+e_term)

h = float(input("Enter starting height (in meters): "))
t = 0.0
y_t = h
v_t = v_t_initial
time =[]
position = []
file = open("para_jump_output.txt", "w")

while (y_t > 0):

    if y_t > 1200:
        
        t+=0.1
        y_t = h - v_t_initial*quad(integrand, 0, t)[0]
        
        time.append(t)
        position.append(y_t)

    if y_t <= 1200 and v_t > v_t_parachute:
        dt = 0.001
        t += dt
        v_t -= .0155
        dy = - 0.5*v_t*dt
        y_t += dy
        time.append(t)
        position.append(y_t)
    h_chute = y_t

    if v_t <= v_t_parachute:
        t += 0.1
        dy = - v_t_parachute*quad(integrand, 0, t)[0]
        y_t = h_chute + dy
        
        time.append(t)
        position.append(y_t)

    if y_t < 0:
            y_t = 0

for index, time in enumerate(time):    
    print(f"{time}, {position[index]}\n")
    file.write(f"{time}, {position[index]}\n")
   
file.close()
