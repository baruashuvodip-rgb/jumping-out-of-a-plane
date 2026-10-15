from math import exp
from scipy.integrate import quad
import para_jump_straight
import para_jump_w_parachute

g = 9.8 #acceleration due to gravity

h = float(input("Enter starting height: "))

para_answer = input("Deploy parachute? y/n:\n")

match para_answer:
    case 'y':
        para_jump_w_parachute.fall_w_parachute(h)

    case 'n':
        para_jump_straight.no_parachute(h)

