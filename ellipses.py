from ssl import OP_NO_RENEGOTIATION
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
from matplotlib.patches import Ellipse, Circle, Wedge
import sys 
import cv2 

#Constants
RADIUS = 1220
PERCENTAGE = int(sys.argv[1])/100
PLOTDIM = RADIUS
#Pyplot setup
f = plt.figure()
ax = plt.gca()
#f.set_figwidth(PLOTDIM)
#f.set_figheight(PLOTDIM) 
#plt.xlim([-PLOTDIM,PLOTDIM])
#plt.ylim([-PLOTDIM,PLOTDIM])


if PERCENTAGE >= 50/100: 
    #Calculate Ellipse Dimensions
    B = (PERCENTAGE - 50/100) * 2 * RADIUS
    print(B)
    ellipse = Ellipse(xy=(RADIUS,RADIUS),height = RADIUS*2, width = B*2,fc='black')
    circle = Circle(xy=(RADIUS,RADIUS),radius = RADIUS, edgecolor = 'g',fc='white')
    semicircle = Wedge(center=(RADIUS,RADIUS),r = RADIUS, theta1 = 270, theta2 = 90, fc='black')

else: 
    PERCENTAGE = 1 - PERCENTAGE
    B = (PERCENTAGE - 50/100) * 2 * RADIUS
    ellipse = Ellipse(xy=(1220,1220),height = RADIUS*2, width = B*2,fc='white')
    circle = Circle(xy=(1220,1220),radius = RADIUS, edgecolor = 'g',fc='black')
    semicircle = Wedge(center=(1220,1220),r = RADIUS, theta1 = 90, theta2 = 270, fc='white')

#add stuff to plot and show
moon = mpimg.imread('moon.jpg',)
moon = cv2.cvtColor(moon,cv2.COLOR_BGR2GRAY)
ax.imshow(moon,cmap='gray',origin='lower')
#ax.add_patch(circle)
ax.add_patch(ellipse)
ax.add_patch(semicircle)
ax.axis("off")
plt.show()