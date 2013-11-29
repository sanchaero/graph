#!/usr/bin/env python

#from __future__ import division
#from matplotlib.patches import Patch
from pylab import * 
from numpy  import *
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt

#~ HNW

#~ g = open('LDOS.txt')
#~ eFermi=-4.3862
#~ eMin = -8.7524#-7.3595
#~ eMax = 0.2476#1.6405
#~ x = arange(0, 25*sqrt(2), 25*sqrt(2)/599.99)

#~ NW+
#~ g = open('LDOSsum+.txt')
#~ eFermi=-3.6460#
#~ eMax =2
#~ eMin = -8
#~ x = arange(0, 25*sqrt(2), 25*sqrt(2)/599.99)
#~ NW-
g = open('LDOSsum.txt')
eFermi=-2.7178
eMax =3.5
eMin = -6.5
x = arange(0, 20*sqrt(2), 20*sqrt(2)/599.99)

buffer = g.readlines()
DATA = zeros( (500,600) )

for i in xrange(len(buffer)):
    temp = buffer[i].split()
    a = int(temp[0])
    b = int(temp[1])
    c = float(temp[2])
    if c <0.000001:
        c = 0.00000001
    DATA[a][b] +=c

tickSet=[pow(10,-i) for i in range(1,4)]
strTickSet=['10$^{-'+str( i )+'}$' for i  in range(1,4)]
g.close()


#real space

#energy 
y = arange(eMin-eFermi, eMax-eFermi, (eMax-eMin)/(500-0.001))
print len(x), len(y)
X,Y = meshgrid(x,y)


subplot(1,1,1)
pcolormesh(X,Y,DATA,norm=LogNorm(vmin=min(tickSet),vmax=max(tickSet)))


cbar=colorbar()
cbar.set_label('Density of States (States/eV/$\AA$$^{-3}$)',fontsize=18,rotation=90)
cbar.set_ticks(tickSet)
cbar.set_ticklabels(strTickSet)

xlabel('Real space ($\AA$)',size=20) #title('title', color='r')
ylabel('Energy (eV)',size=20)
title('Local density of states',size=20)
#axis([0,35.355339059327378,-4,4])
axis([0,20,-3.5,5.5])


show()

