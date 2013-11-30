"""
You can use the proper typesetting unicode minus (see
http://en.wikipedia.org/wiki/Plus_sign#Plus_sign) or the ASCII hypen
for minus, which some people prefer.  The matplotlibrc param
ax1es.unicode_minus controls the default behavior.

The default is to use the unicode minus
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
from mpl_toolkits.axes_grid1.parasite_axes import SubplotHost
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.gridspec as gridspec

import sys,re,string


def readData(inputFile):
    Data=[]
    f=open(inputFile)
    lines=f.readlines()
    nSet=len(lines)/2
    #~ print nSet
    eFermi=[6.207862,5.642064,5.013502]
    i=0
    for i in range(nSet):
        label='band'
        X=[float(x) for x in lines[i*2+0].split()]
        Y=[float(y)-eFermi[i] for y in lines[i*2+1].split()]
        Data.append([label,X,Y])
        i+=1
    f.close()
    return Data
    

    
def draw(file='band.dat'):
    titleFontSize=18
    markerSize=11
    lineWidth=3
    matplotlib.rcParams['axes.unicode_minus'] = False
    fig = plt.figure(figsize=(9.5,7))
    #~ plt.subplots_adjust(top=0.92,bottom=0.08,left =0.1,right =0.95,hspace=0.4,wspace=0.3)
    
        #~ band1
    #~ gs1=gridspec.GridSpec(2,2)
    #~ gs1.update(left=0.1, right=0.47, wspace=0.0)
    ax2 = fig.add_subplot(111)
    
    ax2.tick_params(direction='in', labelleft='on',labelright='off')
    Data=readData(file)

    lineSet=['bo','ro','go']
    i=0
    for data in Data:
        labelt=data[0]
        X=data[1]
        Y=data[2]
        ax2.plot(X,Y,'ko',label=labelt,markersize=5,linewidth=lineWidth,markeredgewidth  =0)
        i+=1
    ax2.yaxis.set_major_locator(MultipleLocator(1))
    ax2.yaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax2.yaxis.set_minor_locator(MultipleLocator(0.1))
    #~ ax2.set_ylim(-7,2)
    ax2.set_ylabel('E (eV)',size=15)

        
    plt.show()
def readBand(file='EIGENVAL'):
    fw=open('bandOUT.txt','w')
    fdat=open('band.dat','w')


    eFermi=0
    k=(0,0,0)
    kold=(0,0,0)
    dk=0.0
    kp=0.0

    K=[]
    En=[]

    f=open(file,'r')
    for i in range(7):
        f.readline()
    for line in f.readlines():

            m= re.match(r'\s+(-*[0-9].[0-9]+E[+-][0-9]+)\s+(-*[0-9].[0-9]+E[+-][0-9]+)\s+(-*[0-9].[0-9]+E[+-][0-9]+)',line)
            if m :
                    """
                    k point distance calculation
                    """
                    k=( float(m.group(1)) , float(m.group(2)) , float(m.group(3)) )
                   
                    if dk < 1000 :
                            dk=pow(pow(k[0]-kold[0],2)+pow(k[1]-kold[1],2)+pow(k[2]-kold[2],2),0.5)
                            if dk>0.2:
                                dk=0
                    else:
                            dk=0
                    kold=k

                    kp=kp+dk
                    #print "matched"
                    #~ if len(band)>0:
                            #~ bands.append(band)
                            #~ band=[]
            else:
                    if len(line)>2:
                            fw.write(str(kp)+'\t'+line[0:len(line)-2]+'\n')
                            K.append(str(kp))
                            En.append(str((float(line.split()[1])-eFermi)))
                            #~ print str(kp)+'\t'+line[0:len(line)-2].strip()
    for i in range(len(K)):
        fw.write(str(K[i])+'\t'+En[i]+'\n')
    for k in K:
        fdat.write(k+' ')
    fdat.write('\n')
    for en in En:
        fdat.write(en+' ')


    f.close()
    fw.close()
    fdat.close()



readBand('EIGENVAL')
draw()