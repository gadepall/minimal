#Code by GVV Sharma
#October 1, 2023
#released under GNU GPL
#Perpendicular Bisectors of a triangle
#Circumcentre and Circumcircle


import sys                                          #for path to external scripts
#sys.path.insert(0, 'codes/CoordGeo')        #path to my scripts
sys.path.insert(0, '/sdcard/github/minimal/codes/CoordGeo')        #path to my scripts
import numpy as np
import mpmath as mp
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


#if using termux
import subprocess
import shlex
#end if

#Center
O = np.array([2,0]).reshape(-1,1)

#Diameter End Points
A = np.array([6,0]).reshape(-1,1)
R = np.linalg.norm(A-O)
B = 2*O-A

#Generating the circle
x_circ= circ_gen(O,R)

#Plotting the circumcircle
plt.plot(x_circ[0,:],x_circ[1,:])

#Generating all lines
x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='Diameter')

#Labeling the coordinates
tri_coords = np.block([[A,B,O]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','O']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('figs/perp-bisect.pdf')
subprocess.run(shlex.split("termux-open figs/perp-bisect.pdf"))
#else
#plt.show()
