# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 11:00:01 2022

@author: Anna Sofie R. Ståle
"""

"""
Forsøg på nyt deviation plot for highpass filter
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Lowpass_data=pd.read_csv('high pass filter values.csv',sep=';',decimal=',')
Lowpass_data['Frq']=Lowpass_data['Frq'].astype(float)
Lowpass_data['Ch2Mag']=Lowpass_data['Ch2Mag'].astype(float)
Lowpass_data['Ch2Phase']=Lowpass_data['Ch2Phase'].astype(float)
Frequency=Lowpass_data['Frq'].to_numpy()
Magnitude=Lowpass_data['Ch2Mag'].to_numpy()
Phase=Lowpass_data['Ch2Phase'].to_numpy()


def mag(f=Frequency):
    m = 20*np.log10((0.0002*2*np.pi*f)/(np.sqrt(1+0.0002**2*2**2*np.pi**2*f**2)))
    return m

def phase(f=Frequency):
    p = np.degrees(np.arctan(1/(0.0002*2*np.pi*f)))
    return p

#Forskel ved første frekvens:
print(Magnitude[0]-mag(10))

#Forskel ved cutoff frequency:
#print(Magnitude[634])
print(Magnitude[634]-mag(797.9946872679769))

#Forskel ved største frequency:
print(Magnitude[1000]-mag(10000))


#Phaseforskel ved første frekvens:
print(Phase[0]-phase(10.00000000000001))

#Phaseforskel ved cutoff frequency:
print(Phase[634]-phase(797.9946872679769))

#Phaseforskel ved største frequency:
print(Phase[1000]-phase(10000))





"""
plt.figure(figsize=(15,9))
plt.subplot(2,1,1)
plt.plot(Frequency,Magnitude)
plt.xscale("log")
plt.grid(True)
plt.title("The magnitude Plot",fontsize=20)
plt.plot(Frequency,mag(),linestyle=':',color='orange')
plt.xlabel("F [Hz]",fontsize=20)
plt.ylabel("Magnitude [dB]",fontsize=20)
plt.tight_layout()

plt.subplot(2,1,2)
plt.plot(Frequency,Phase)
plt.xscale("log")
plt.grid(True)
plt.title("The phase Plot",fontsize=20)
plt.plot(Frequency,phase(),linestyle=':',color='orange')
plt.xlabel("F [Hz]",fontsize=20)
plt.ylabel("Phase Angle [Deg]",fontsize=20)
plt.tight_layout()
"""


plt.figure(figsize=(15,9))
plt.subplot(2,1,1)
plt.plot(Frequency,Magnitude-mag(),label='Deviation')
plt.axvline(x=795.77,linestyle=':',color='orange',label='Cutoff frequency')
plt.xscale("log")
plt.grid(True)
plt.title("Deviation in the magnitude Plot",fontsize=20)
plt.xlabel("f [Hz]",fontsize=20)
plt.ylabel("Magnitude [dB]",fontsize=20)
plt.tight_layout()
plt.legend()


plt.subplot(2,1,2)
plt.plot(Frequency,Phase-phase(),label='Deviation')
plt.axvline(x=795.77,linestyle=':',color='orange',label='Cutoff frequency')
plt.xscale("log")
plt.grid(True)
plt.title("Deviation in the phase Plot",fontsize=20)
plt.xlabel("f [Hz]",fontsize=20)
plt.ylabel("Phase Angle [Deg]",fontsize=20)
plt.tight_layout()
plt.legend()
#plt.savefig('DeviationExp2HighPass.png',dpi=500)

