# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 10:44:49 2022

@author: marti
"""

import numpy as np
import matplotlib.pyplot as plt

#############################################################

# For at ændre hvordan plottene ser ud skal der kun ændres ved 
#frekvensen her under
frequency=1 #Hz
frequency2=1000000 #Hz


#############################################################

t=np.linspace(0, 10*np.pi,1000)

fq=frequency*2*np.pi
tp=(2*np.pi)/fq


fq2=frequency2*2*np.pi
tp2=(2*np.pi)/fq2


tau=0.0002



def sin(t): #input til filtret
    return np.sin(t)

#Highpass
def HPphase(t): #faseforskydning ved Highpass
    return -np.arctan(1/(fq*tau))   
def HPmag(t): #Ampitydemultiplier ved Highpass
    return (abs(tau)*abs(fq))/(np.sqrt(1+(tau**2*(fq)**2)))

#Highpass2
def HP2phase(t): #faseforskydning ved Highpass
    return -np.arctan(1/(fq2*tau))   
def HP2mag(t): #Ampitydemultiplier ved Highpass
    return (abs(tau)*abs(fq2))/(np.sqrt(1+(tau**2*(fq2)**2)))

#Lowpass
def LPphase(t): #faseforskydning ved Lowpass
    return -np.arctan(-fq*tau)   
def LPmag(t): #Ampitydemultiplier ved Lowpass
    return 1/(np.sqrt(1+(tau**2*(fq)**2)))

#Lowpass2
def LP2phase(t): #faseforskydning ved Lowpass
    return -np.arctan(-fq2*tau)   
def LP2mag(t): #Ampitydemultiplier ved Lowpass
    return 1/(np.sqrt(1+(tau**2*(fq2)**2)))

#Plot


#Highpass
def HP():
    plt.subplot(1,2,1)
    plt.plot(t/fq*1000,sin(t),color='dodgerblue')
    plt.plot((t+HPphase(t))/fq*1000,sin(t)*HPmag(t),color='r',linewidth=2, linestyle=':')
    plt.xlabel('Time [ms]')
    plt.xticks(np.arange(0,(tp*5+0.000001)*1000,tp*1000))
    plt.ylabel('Gain [relative]')
    plt.yticks()
    plt.legend([r'$V_{in}$',r'$V_{out}$'], loc=1)
    plt.grid()
    plt.title(f'Highpass Filter - {frequency}Hz',size=14)
    
    plt.subplot(1,2,2)
    plt.plot(t/fq2*1000,sin(t),color='dodgerblue')
    plt.plot((t+HP2phase(t))/fq2*1000,sin(t)*HP2mag(t),color='r',linewidth=2, linestyle=':')
    plt.xlabel('Time [ms]')
    plt.xticks(np.arange(0,(tp2*5+0.000001)*1000,tp2*1000))
    plt.ylabel('Gain [relative]')
    plt.yticks()
    plt.legend([r'$V_{in}$',r'$V_{out}$'], loc=1)
    plt.grid()
    plt.title(f'Highpass Filter - {frequency2}Hz',size=14)
    
    fig = plt.gcf()
    fig.set_size_inches(12, 4)
    fig.savefig(f'Highpass-{frequency,frequency2}.png', dpi=500)


#Lowpass
def LP():
    plt.subplot(1,2,1)
    plt.plot(t/fq*1000,sin(t),color='dodgerblue')
    plt.plot((t+LPphase(t))/fq*1000,sin(t)*LPmag(t),color='r',linewidth=2, linestyle=':')
    plt.xlabel('Time [ms]')
    plt.xticks(np.arange(0,(tp*5+0.000001)*1000,tp*1000))
    plt.ylabel('Gain [relative]')
    plt.legend([r'$V_{in}$',r'$V_{out}$'], loc=1)
    plt.grid()
    plt.title(f'Lowpass Filter - {frequency}Hz',size=14)
    
    plt.subplot(1,2,2)
    plt.plot(t/fq2*1000,sin(t),color='dodgerblue')
    plt.plot((t+LP2phase(t))/fq2*1000,sin(t)*LP2mag(t),color='r',linewidth=2, linestyle=':')
    plt.xlabel('Time [ms]')
    plt.xticks(np.arange(0,(tp2*5+0.000001)*1000,tp2*1000))
    plt.ylabel('Gain [relative]')
    plt.legend([r'$V_{in}$',r'$V_{out}$'], loc=1)
    plt.grid()
    plt.title(f'Lowpass Filter - {frequency2}Hz',size=14)
    
    fig = plt.gcf()
    fig.set_size_inches(12, 4)
    fig.savefig(f'Lowpass-{frequency,frequency2}.png', dpi=500)

#call the function bellow here -Only one at the time


#HP()
#LP()
