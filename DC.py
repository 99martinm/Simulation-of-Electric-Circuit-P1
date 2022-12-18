# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 15:04:00 2022

@author: martin

To make the 4 diffrent plots, the functions have to be called,
their names are: Exp(), Model(), Combp(), Diff()

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


Values = pd.read_csv(r'DC_VALUES.csv',sep=';',decimal=',')

pd.set_option("display.max.columns", None)
Values.head()
print(Values)

Values['Time']=Values['Time'].astype(float)
Values['Capacitor']=Values['Capacitor'].astype(float)
Values['Squarewave']=Values['Squarewave'].astype(float)


time=Values['Time'].to_numpy()
Capacitor=Values['Capacitor'].to_numpy()
Squarewave=Values['Squarewave'].to_numpy()


######################################################################################


def Exp():
    # Plot af forsøg
    plt.subplot(1,2,1)
    plt.plot(time[:1601],1+Capacitor[:1601],'orange')
    plt.plot(time[:1601],1+Squarewave[:1601],'k--',linewidth=1)
    plt.xlabel('Time [ms]')
    plt.ylabel('Voltage [V]')
    plt.legend(['Capacitor','Squarevave'], loc=7)
    plt.title('Charging of the capacitor',size=16)
    
    plt.subplot(1,2,2)
    plt.plot(time[:1601],1+Capacitor[1600:3201],'orange')
    plt.plot(time[:1601],1+Squarewave[1600:3201],'k--',linewidth=1)
    plt.xlabel('Time [ms]')
    plt.ylabel('Voltage [V]')
    plt.legend(['Capacitor','Squarevave'], loc=7)
    plt.title('Discharging of the capacitor',size=16)
    
    fig = plt.gcf()
    fig.set_size_inches(12, 4)
    fig.savefig('EXP.png', dpi=500)

def Model():
    #Plot af model
    plt.subplot(1,2,1)
    plt.plot(time[:1601],(2*(1-np.exp((-time[:1601]/1000/0.0002)))),color='dodgerblue')
    plt.plot(time[:1601],1+Squarewave[:1601],'k--',linewidth=1)
    plt.xlabel('Time [ms]')
    plt.ylabel('Voltage [V]')
    plt.legend(['Mathematical model','Squarevave'], loc=7)
    plt.title('Model for charging of the capacitor',size=16)
    
    
    plt.subplot(1,2,2)
    plt.plot(time[:1601],(2*(np.exp((-time[:1601]/1000/0.0002)))),color='dodgerblue')
    plt.plot(time[:1601],1+Squarewave[1600:3201],'k--',linewidth=1)
    plt.xlabel('Time [ms]')
    plt.ylabel('Voltage [V]')
    plt.legend(['Mathematical model','Squarevave'], loc=7)
    plt.title('Model for discharging of the capacitor',size=16)
    
    fig = plt.gcf()
    fig.set_size_inches(12, 4)
    fig.savefig('Math.png', dpi=500)

def Combo():
    #Plot af model and Experiment
    plt.subplot(1,2,1)
    plt.plot(time[:1601],1+Capacitor[:1601],'orange')
    plt.plot(time[:1601],(2*(1-np.exp((-time[:1601]/1000/0.0002)))),color='dodgerblue',linestyle=':',linewidth=3)
    plt.plot(time[:1601],1+Squarewave[:1601],'k--',linewidth=1)
    plt.xlabel('Time [ms]')
    plt.ylabel('Voltage [V]')
    plt.plot(.2,2*(1-0.368), marker='x',color='r')
    plt.legend(['Capacitor','Mathematical model','Squarevave','t=\u03C4'], loc=7)
    plt.title('Comparison of charging',size=16)
    
    plt.subplot(1,2,2)
    plt.plot(time[:1601],1+Capacitor[1600:3201],'orange')
    plt.plot(time[:1601],(2*(np.exp((-time[:1601]/1000/0.0002)))),color='dodgerblue',linestyle=':',linewidth=3)
    plt.plot(time[:1601],1+Squarewave[1600:3201],'k--',linewidth=1)
    plt.xlabel('Time [ms]')
    plt.ylabel('Voltage [V]')
    plt.plot(.2,2*0.368, marker='x',color='r')
    plt.legend(['Capacitor','Mathematical model','Squarevave','t=\u03C4'], loc=7)
    plt.title('Comparison of discharging',size=16)
    
    fig = plt.gcf()
    fig.set_size_inches(12, 4)
    fig.savefig('Combo.png', dpi=500)

def Diff():
    plt.subplot(1,2,1)
    plt.scatter(time[:1601],(1+Capacitor[:1601]-(2*(1-np.exp((-time[:1601]/1000/0.0002)))))*1000,s=2,color='g')
    plt.xlabel('Time [ms]')
    plt.ylabel('Voltage [mV]')
    plt.title('Deviation of charging',size=16)
    
    plt.subplot(1,2,2)
    plt.scatter(time[:1601],(1+Capacitor[1600:3201]-(2*(np.exp((-time[:1601]/1000/0.0002)))))*1000,s=2,color='g')
    plt.xlabel('Time [ms]')
    plt.ylabel('Voltage [mV]')
    plt.title('Deviation of discharging',size=16)
    
    fig = plt.gcf()
    fig.set_size_inches(12, 4)
    fig.savefig('Diff.png', dpi=500)

#call the function bellow here -Only one at the time

#Exp()
#Model()
#Combo()
#Diff()