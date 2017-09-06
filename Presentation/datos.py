#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from __future__ import division     
import numpy as np
import matplotlib.pyplot as plt

#Plotting
plt.rc('font', family='serif',size=26)
#plt.grid()
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

plt.figure(1)
plt.xlabel(r'$\psi$',fontsize=36)
plt.ylabel(r'$\frac{V|_\psi}{V}$',rotation=0,fontsize=36)

x=np.linspace(0,1,1000)
def f(x): return 1-0.21*x -0.01*x**2
plt.plot(x, f(x))
#plt.title(u'Campo magnético vs intensidad aplicada')
plt.ylim(0,1.2)

ax = plt.gca()
yticks = ax.yaxis.get_major_ticks() 
yticks[0].label1.set_visible(False)
xticks = ax.xaxis.get_major_ticks() 
ax.yaxis.set_label_coords( -0.2,0.8)
ax.xaxis.set_label_coords( 0.9,-0.1)

##plt.text(190,10.2,'w=120') 
#plt.show()
plt.savefig('graph.eps', format='eps',dpi=100)

#plt.legend(numpoints=1)
