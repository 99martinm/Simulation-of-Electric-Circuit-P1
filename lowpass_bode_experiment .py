#Computing the bodeplots of the experimental data for the lowpass filter
#Packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Transfer function
def Filter(f,R,C):                     # Define the Filter function that corresponds to the low pass RC filter.
    omega = 2*np.pi*f
    vout=( 1./(1j*R*omega*C+1.))
    return(vout)
#Treating the data collected from Waveforms
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
#The values of the resistor and capacitor
R=2000. # 2kOhm
C=0.1e-6  # 1µF
#Caculating and printing the cutoff frequency
F_cut = 1./(2.*np.pi*R*C)
print("========================================")
print("Filter cut off frequency is: {:7.2f} Hz".format(F_cut))
print("========================================")
#Plotting the magnitude function
plt.figure(figsize=(15,9)) # Make a figure, and make it bigger.
plt.subplot(2,1,1)         # First subplot in the figure with (2 columns, 1 row, 1st subplot)
plt.plot(Frequency,Magnitude) # Plot the amplitude, the absolute of the complex number
#plt.plot([F_cut,F_cut],[0,-35],color="red",label="Cut off frequency")  # plot a line for the filter cut frequency
plt.axvline(x=F_cut, color='r', linestyle='dashed',label='Cutoff Frequency') #Plots a vertical at the cutoff frequency
plt.title("Magnitude Plot",fontsize=20)
plt.xlabel("f [Hz]",fontsize=20)
plt.ylabel("Magnitude [dB]",fontsize=20)
plt.xscale("log")           # Set x to a log scale
plt.xticks(fontsize=20) #Set fontsize on numbers on the x-axis
plt.yticks(fontsize=20) #Set fontsize on numbers on the y-axis
plt.grid(True)
plt.legend()
plt.tight_layout()          # Automatically adjust spacing between the 2 plots so they do not overlap
#Plotting the phase plot
plt.subplot(2,1,2)
plt.plot(Frequency,Phase) # Plot the amplitude, the absolute of the complex number
plt.axvline(x=F_cut, color='r', linestyle='dashed',label='Cutoff Frequency') #Plots a vertical at the cutoff frequency
plt.axhline(y=-45, color='b', linestyle='dashed',label= '-45 Degrees') #Plots a horizontal line at -45 degrees
plt.title("Phase plot",fontsize=20)
plt.xlabel("f [Hz]",fontsize=20)
plt.ylabel("Phase Angle [Deg]",fontsize=20)
plt.xscale("log")
plt.xticks(fontsize=20) #Set fontsize on numbers on the x-axis
plt.yticks(np.arange(-90,0,15),fontsize=20) #Set fontsize on numbers on the y-axis
plt.grid(True)
plt.legend()
plt.tight_layout()          # Automatically adjust spacing between the 2 plots so they do not overlap
plt.show()