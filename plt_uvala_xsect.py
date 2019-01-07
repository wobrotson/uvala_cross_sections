# script to plot uvala cross-sectional profiles

# read csv file

import numpy as np
import pandas as pd

df = pd.read_csv('U2_profs.csv', header=0)

# sort data into respective profiles by prof_id

pA = df['prof_id']== 1
U2A = df[pA]

pB = df['prof_id']== 2
U2B = df[pB]

pC = df['prof_id']== 3
U2C = df[pC]

# plot data
%matplotlib inline 
from matplotlib import pyplot as plt

ax1 = plt.axes()
ax1.plot(U2A.cds2d, U2A.DSM2016, color=[.6,.25,.31])
plt.xlabel('distance [m]',fontsize=12)
plt.ylabel('elevation[m]',fontsize=12)
plt.text(-30,-390,'A',fontsize=12)
plt.text(1390,-406,"A'",fontsize=12)

ax2 = plt.axes([0.52, 0.62, 0.35, 0.2])
ax2.plot(U2B.cds2d, U2B.DSM2016, color=[.6,.25,.31])
ax2.tick_params(labelsize=8)
ax3.labelsize=8
plt.text(0,-396,'B',fontsize=10)
plt.text(580,-383,"B'",fontsize=10)
plt.title('Profile B', fontsize=10)

ax3 = plt.axes([0.2, 0.19, 0.27, 0.2])
ax3.plot(U2C.cds2d, U2C.DSM2016, color=[.6,.25,.31])
ax3.tick_params(labelsize=8)
ax3.labelsize=8
plt.text(0,-397,'C',fontsize=10)
plt.text(450,-422,"C'",fontsize=10)
plt.title('Profile C', fontsize=10)

#save figure as png and svg
plt.savefig('u2_xsect_plt.svg', bbox_inches='tight')
plt.savefig('u2_xsect_plt.png', bbox_inches='tight')