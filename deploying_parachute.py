from math import exp
from scipy.integrate import quad

g = 9.8 #acceleration due to gravity

def integrand(t):
    e_term = exp(-2*g*t/v_terminal)
    num = 1 - e_term    #numerator of integrand
    denom = 1 + e_term  #denominator of integrand
    return num/denom

v_term_initial = 54.0 #initial terminal velocity, without parachute
v_term_final = 7.6 #final terminal velocity, with parachute fully deployed
a_deployment = (v_term_initial - v_term_final)/3

h = float(input("Enter starting height: "))
y = h
t = 0.0
v_terminal = v_term_initial

file = open("parajump_y_vs_t.txt","w")

while(y > 1200.0):
    
    y = h - v_terminal*quad(integrand, 0, t)[0]
    file.write(f"{t} {y} {v_terminal}\n")
    t += 0.1

    if(y <= 1200.0):
        deploy_height = y
        deploy_time = t

dt = 3e-3/(v_term_initial - v_term_final) #time interval calculated such that if parachute takes 3 seconds to deploy, /
                                            #then terminal velocity changes by 1e-3 for every time interval

y = deploy_height
v_init = v_term_initial

while(y <= 1200.0 and v_terminal > v_term_final):
    
    dy = v_init*dt - 0.5*a_deployment*dt*dt
    y -= dy
    file.write(f"{t} {y} {v_init}\n")
    t += dt
    v_init -= 1e-3

    if(v_init <= v_term_final):
            v_terminal = v_term_final
            fully_deployed_height = y
            fully_deployed_time = t
    

while(y > 0.0 and v_terminal == v_term_final):
    
    h = fully_deployed_height
    t += 0.1

    y -= v_terminal*0.1
        
    if(y < 0.0):
        y = 0.0
        
    file.write(f"{t} {y} {v_terminal}\n")
    

file.close()

