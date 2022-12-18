#Computing plot of the comparision of the experimental data 
#and the mathematical model for the lowpass filter.
#Packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Transfer function
def Filter(f,R,C):                     # Define the Filter function that corresponds to the low pass RC filter.
    omega = 2*np.pi*f
    vout=( 1./(1j*R*omega*C+1.))
    return(vout)
f = np.linspace(10,10000,1000) #Frequnecy inputs for the model
#Treating the experimental data
Lowpass_data=pd.read_csv('low pass filter values.csv',sep=';',decimal=',')
pd.set_option("display.max.columns", None)
Lowpass_data.head()
print(Lowpass_data)
Lowpass_data['Frq']=Lowpass_data['Frq'].astype(float)
Lowpass_data['Ch2Mag']=Lowpass_data['Ch2Mag'].astype(float)
Lowpass_data['Ch2Phase']=Lowpass_data['Ch2Phase'].astype(float)
print(type(Lowpass_data['Frq']))
Frequency=Lowpass_data['Frq'].to_numpy()
Magnitude=Lowpass_data['Ch2Mag'].to_numpy()
Phase=Lowpass_data['Ch2Phase'].to_numpy()
print(type(Frequency))
#Setting the values of the resistor and the capacitor
R=2000. # 2kOhm
C=0.1e-6  # 1µF
#Output voltage
vout_c = Filter(f,R,C)
#Calculating and printing the cutoff frequency
F_cut = 1./(2.*np.pi*R*C)
print("========================================")
print("Filter cut off frequency is: {:7.2f} Hz".format(F_cut))
print("========================================")
#Magnitude function
y_db = 20*np.log10(np.abs(vout_c))
#Magnitude plot
plt.figure(figsize=(15,9)) # Make a figure, and make it bigger.
plt.subplot(2,1,1)         # First subplot in the figure with (2 columns, 1 row, 1st subplot)
plt.plot(Frequency,Magnitude,label='Experimental Data',linewidth=3,color='orange') # Experiemental data
plt.plot(f,y_db,label='Mathematical Model',linewidth=3,linestyle=':',color='dodgerblue') #Mathematical model
plt.axvline(x=F_cut, color='r', linestyle='dashed',label='Cutoff Frequency') #Plots a line at the cutoff frequency
plt.axhline(y=-3, color='g', linestyle='dashed',label='-3 dB') #Plots a line at -3 dB
plt.title("Magnitude Plot",fontsize=20)
plt.xlabel("f [Hz]",fontsize=20)
plt.ylabel("Magnitude [dB]",fontsize=20)
plt.xscale("log")           # Set x to a log scale
plt.xticks(fontsize=20) #Set fontsize on numbers on the x-axis
plt.yticks(fontsize=20) #Set fontsize on numbers on the y-axis
plt.grid(True)
plt.tight_layout()          # Automatically adjust spacing between the 2 plots so they do not overlap
plt.legend(loc=1,fontsize='x-large')
#Phase plot
plt.subplot(2,1,2)
plt.plot(Frequency,Phase,label='Experimental Data',linewidth=3,color='orange') # Experimental data
plt.plot(f,np.angle(vout_c,deg=True),label='Mathematical Model',linewidth=3,linestyle=':',color='dodgerblue') #Mathematical model
plt.axvline(x=F_cut, color='r', linestyle='dashed',label='Cutoff Frequency') #Plots a line at the cutoff frequency
plt.axhline(y=-45, color='m', linestyle='dashed',label='-45 Deg') #Plots a line at -45 deg
plt.title("Phase plot",fontsize=20)
plt.xlabel("f [Hz]",fontsize=20)
plt.ylabel("Phase Angle [Deg]",fontsize=20)
plt.xscale("log")
plt.xticks(fontsize=20) #Set fontsize on numbers on the x-axis
plt.yticks(np.arange(-90,0,15),fontsize=20) #Set fontsize on numbers on the y-axis
plt.grid(True)
plt.tight_layout()          # Automatically adjust spacing between the 2 plots so they do not overlap
plt.legend(loc=1,fontsize='x-large')
plt.show()

