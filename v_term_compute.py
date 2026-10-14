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

v_terminal = v_term_initial

def instant_velocity(t, v_t):
    v = - v_t*integrand(t)
    return v

t_init = 55.7
v_init = instant_velocity(t_init, v_term_initial)
t_final = 58.7

print(v_init)