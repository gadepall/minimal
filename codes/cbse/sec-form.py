#Code by GVV Sharma
#September 29, 2026
#released under GNU GPL
#Section formula
#Rank


import sys                                          #for path to external scripts
sys.path.insert(0, '/sdcard/github/minimal/codes/CoordGeo')        #path to my scripts
import numpy as np
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

#Triangle vertices
A = np.array([1,2]).reshape(-1,1)
B = np.array([2,3]).reshape(-1,1) 
C = 1/5*np.array([8,13]).reshape(-1,1) 


#Collinearity check
mat=np.block([[1,1,1],[A,B,C]])
print(mat, LA.matrix_rank(mat))

#Generating all lines
x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

#Labeling the coordinates
tri_coords = np.block([[A,B,C]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C']
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
plt.savefig('figs/section.pdf')
subprocess.run(shlex.split("termux-open figs/section.pdf"))
#else
#plt.show()

