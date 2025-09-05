#Initial design of a numerical cordic algorithm in python. 8/26/25
#
#Note:(09/3/25) The sum of my arctan lookup table only reaches up to about +/-100 degrees 
#on the unit circle. Therefore, I am now implementing a quadrant check. ~HD

import numpy as np 
import matplotlib.pyplot as plt



#input to my cordic design is the number of iterations and the angle.Max number of iterations is 11
def cordic(n, theta):


	SCALING_FACTOR = 0.6072  #this is a scaling factor that comes from taking out a cos(theta) from the rotation matrix in cordic

	sign = 0                 #sign of the rotation vector

	ARCTAN_LUT = [45, 26.565, 14.036, 7.125, 3.576, 1.7899, 0.8951, 0.44776, 0.2238, 0.1119, 0.05595]  #11 precomputed values of arctan(2^-1) which the amount we rotate each time

	#[x_old, y_old] = [[1,0],[0,0]]   #starting position of the rotation vector
	x_old = [1,0]
	y_old = [0,0]

	quad_check_flag = 0     #flag that checks quadrant
	theta_diff = theta - 90    #calculate the difference between our rotation angle and 90 degrees


	ang_err = theta          #this is the initial error at the beginning of the algorithm since we have zero rotation 
	ang_sum = 0              #the sum of the arctan(theta) value after each iteration
	[x, y] = [ [],[] ]       #old iterations vector 


	for i in range(n):

		if (abs(theta) > 100 and theta_diff > 11 and theta_diff <= 190 and quad_check_flag == 0):
			theta = abs(90 - theta_diff)    #remap the angle onto quadrant 1
			quad_check_flag = 1
		elif(theta_diff > 180 and  quad_check_flag == 0):
			theta = 360 - theta
			quad_check_flag = 1

		if theta > ang_sum:
			sign = 1
			ang_sum += ARCTAN_LUT[i] * sign
			ang_err = theta - ang_sum
		else: 
			sign = -1
			ang_sum += ARCTAN_LUT[i] * sign
			ang_err = theta - ang_sum


		if i % 2 == 0:
			x_old[1] = x_old[0] - (sign * 2**(-i) * y_old[0])
			y_old[1] = y_old[0] + (sign * 2**(-i) * x_old[0])
			#print(x_old[1]) 
		else:
			x_old[0] = x_old[1] - (sign * 2**(-i) * y_old[1])
			y_old[0] = y_old[1] + (sign * 2**(-i) * x_old[1])
			#print(x_old[0] )

	if (theta_diff >= 12 and theta_diff <= 89):
		quad_sign_x = -1							#<====   quadrant two
		quad_sign_y =  1
	elif (theta_diff >= 90 and theta_diff <= 190):  #Since the arctan(2^-i) LUT only reaches +/- 100 degrees we have to let our boundaries overlap
													#in the 3rd and 4th quadrant. Otherwise we get flipped values for X
		quad_sign_x = -1							#<====   quadrant three
		quad_sign_y =  -1 
	elif (theta_diff > 190 and theta_diff <= 269):
		quad_sign_x = 1								#<====   quadrant four
		quad_sign_y = -1
	else:
		quad_sign_x = 1								#<====   quadrant one
		quad_sign_y =  1 


	x = x_old[0] *SCALING_FACTOR *quad_sign_x
	y = y_old[0] *SCALING_FACTOR *quad_sign_y
	return x, y


print(cordic(10, 0))
print(cordic(10, -180))

#1, 0.5, 0.25, 0.125, 0.0625, 0.03125
#x_values  = [1, 0.5,  ]
#y values  = [1, 1.75, ]