from numpy import exp
from scipy.integrate import quad

g = 9.81  # acceleration due to gravity in m/s^2

v_term_initial = 54.0 #initial terminal velocity, without parachute
v_term_final = 7.6 #final terminal velocity, with parachute fully deployed
a_deployment = (v_term_initial - v_term_final)/3
v_terminal = v_term_initial

def integrand(t):
    e_term = exp(-2*g*t/v_terminal)
    return (1-e_term)/(1+e_term)

def fall_w_parachute(h):
    v_terminal = v_term_initial
    dv = float(input("Enter velocity increment during parachute deployment: "))
    y = h
    t = 0.0

    file = open("para_jump_output.txt","w")

    while(y > 1200.0):
            
        y = h - v_terminal*quad(integrand, 0, t)[0]
        file.write(f"{t} {y} {v_terminal}\n")
        t += 0.1

        if(y <= 1200.0):
            deploy_height = y
            deploy_time = t

    dt = 3*dv/(v_term_initial - v_term_final) #time interval calculated such that if parachute takes 3 seconds to deploy, /
                                                #then terminal velocity changes by dv for every time interval

    y = deploy_height
    v_init = v_term_initial

    while(y <= 1200.0 and v_terminal > v_term_final):
            
        dy = v_init*dt - 0.5*a_deployment*dt*dt
        y -= dy
        file.write(f"{t} {y} {v_init}\n")
        t += dt
        v_init -= dv

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

    deployment_time = fully_deployed_time - deploy_time
    deployment_height = deploy_height - fully_deployed_height
    print("Parachute took",deployment_time,"seconds to deploy fully. During this time the parachutist falls", deployment_height, "meters.")