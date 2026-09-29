#Code by GVV Sharma
#September 29, 2026
#released under GNU GPL
#Mid points of a quadrilateral
#form a parallelogram


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

#Quadrilateral vertices
A = np.array([-1,-1]).reshape(-1,1)
B = np.array([-1,6]).reshape(-1,1) 
C = np.array([3,6]).reshape(-1,1) 
D = np.array([3,-1]).reshape(-1,1) 

#Quadrilateral mid points
Q = (B+C)/2
R = (C+D)/2
P = (A+B)/2
S = (A+D)/2

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_AD = line_gen(A,D)
x_PQ = line_gen(P,Q)
x_QR= line_gen(Q,R)
x_SR= line_gen(R,S)
x_SP= line_gen(P,S)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_SR[0,:],x_SR[1,:],label='$SR$')
plt.plot(x_SP[0,:],x_SP[1,:],label='$SP$')

#Labeling the coordinates
tri_coords = np.block([[A,B,C,D,P,Q,R,S]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','P','Q','R','S']
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
plt.savefig('figs/bisect.pdf')
subprocess.run(shlex.split("termux-open figs/bisect.pdf"))

