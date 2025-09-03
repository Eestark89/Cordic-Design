import numpy 
import matplotlib.pyplot as plt

import matplotlib.animation as animation

from cordic_main import cordic

theta = 0
iterations = 10
x = 0
y = 0

increment = 0


while theta < 360:
	x,y = cordic(iterations, theta)
	theta += 1

	#plt.figure()
	plt.stem(theta, x)
	#plt.stem(theta,y)
	plt.pause(.0001)

plt.show()

