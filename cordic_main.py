#Initial design of a numerical cordic algorithm in python. 8/26/25
#

import numpy as np 
import matplotlib.pyplot as plt

SCALING_FACTOR = 0.6072      #this is a scaling factor that comes from taking out a cos(theta) from the rotation matrix in cordic
theta = 0                     
n =  0                       #number of iterations n
sign = [-1, 1]               #sign of the rotation vector
theta = 45                   #angle by which we want to rotate the vector
[x, y] = [1,0]               #starting position of the rotation vector


