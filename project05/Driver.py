from __future__ import division

from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import pylab
import scipy
import numpy as np

# functions used 
dot = scipy.dot
sin = scipy.sin
cos = scipy.cos

plot = pylab.plot
grid = pylab.grid
axis = pylab.axis
rad = lambda ang: ang*scipy.pi/180

# Function that returns coordnitates of rotated img of shape
def Rotate2D(pts, cnt, ang=scipy.pi/4):
    return dot(pts - cnt, scipy.array([ [cos(ang),sin(ang)], [-sin(ang),cos(ang)] ]) )+cnt

# pts == points or coordinates of desired shape
# points +1(x,y) to close the Polygon shape

# pts = scipy.array([[0,0],[6,0], 
				   # [2,6],[0,0]]) #  triangle

pts = scipy.array([[-6,0], [-6,-3],
					[6,-3],[6,0], 
					[3, 6],[-3,6], [-6,0]]) # hex coord


# plot(*pts.T,lw=5,color='0.5')   


for ang in scipy.arange( 0, 2*scipy.pi, scipy.pi/8):  # loop to keep plotting shape
    ots = Rotate2D(pts, scipy.array([2.0,3.0]), ang)  # call function to get new set of points
    pylab.plot(*ots.T, color='0.2') #  color '0.2' keeps it B&W
    
pylab.axis('image')
grid(False) 	# Get rid of grid lines when plotting


frame = pylab.gca()
frame.axes.get_xaxis().set_ticks([])  # takes of x coord tick marks
frame.axes.get_yaxis().set_ticks([])  # takes of y coord tick marks
frame.axes.set_ylim(-16,16)  # creates a screen grid with y limit of +/- 16
frame.axes.set_xlim(-16,16)  # creates a screen grid with x limit of +/- 16


plt.savefig('final_print.svg',linestyle = '')
plt.show()  

