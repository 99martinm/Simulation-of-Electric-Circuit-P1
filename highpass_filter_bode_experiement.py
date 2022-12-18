#Computing the bodeplot of the experimental data for the highpass filter
#Packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Definition of the transfer function
def Filter(f,R,C):                     # Define the Filter function that corresponds to the low pass RC filter.
    omega = 2*np.pi*f
    vout=( 1./(1j*R*omega*C+1.))
    return(vout)
#Treats data from Excel sheet with extracted values from Waveforms
Highpass_data=pd.read_csv('high pass filter values.csv',sep=';',decimal=',')
pd.set_option("display.max.columns", None)
Highpass_data.head()
print(Highpass_data)
Highpass_data['Frq']=Highpass_data['Frq'].astype(float)
Highpass_data['Ch2Mag']=Highpass_data['Ch2Mag'].astype(float)
Highpass_data['Ch2Phase']=Highpass_data['Ch2Phase'].astype(float)
print(type(Highpass_data['Frq']))
Frequency=Highpass_data['Frq'].to_numpy()
Magnitude=Highpass_data['Ch2Mag'].to_numpy()
Phase=Highpass_data['Ch2Phase'].to_numpy()
print(type(Frequency))
#Sets the value of the resistor and the capacitor
R=2000. # 2kOhm
C=0.1e-6  # 1µF
#Calculates and prints the cutoff frequency
F_cut = 1./(2.*np.pi*R*C)
print("========================================")
print("Filter cut off frequency is: {:7.2f} Hz".format(F_cut))
print("========================================")
#Magnitude plot
plt.figure(figsize=(15,9)) # Make a figure, and make it bigger.
plt.subplot(2,1,1)         # First subplot in the figure with (2 columns, 1 row, 1st subplot)
plt.plot(Frequency,Magnitude) # Plot the amplitude, the absolute of the complex number
plt.axvline(x=F_cut, color='r', linestyle='dashed') #Plots a vertical line at the cutoff frequency
plt.title("Magnitude Plot",fontsize=20)
plt.xlabel("f [Hz]",fontsize=20)
plt.ylabel("Magnitude [dB]",fontsize=20)
plt.xscale("log")           # Set x to a log scale
plt.xticks(fontsize=20) #Set fontsize on numbers on the x-axis
plt.yticks(fontsize=20) #Set fontsize on numbers on the y-axis
plt.grid(True)
plt.tight_layout()          # Automatically adjust spacing between the 2 plots so they do not overlap
#Phaseplot
plt.subplot(2,1,2)
plt.plot(Frequency,Phase) # Plot the amplitude, the absolute of the complex number
plt.axvline(x=F_cut, color='r', linestyle='dashed') #Plots a vertical line at the cutoff frequency
plt.axhline(y=45, color='b', linestyle='dashed') #Plots a horizontal line a 45 degrees
plt.title("Phase plot",fontsize=20)
plt.xlabel("f [Hz]",fontsize=20)
plt.ylabel("Phase Angle [Deg]",fontsize=20)
plt.xscale("log")
plt.xticks(fontsize=20) #Set fontsize on numbers on the x-axis
plt.yticks(np.arange(0,105,15),fontsize=20) #Set fontsize on numbers on the y-axis
plt.grid(True)
plt.tight_layout()          # Automatically adjust spacing between the 2 plots so they do not overlap
plt.show()