#Computing plot of the comparision of the experimental data 
#and the mathematical model for the highpass filter.
#Packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Transfer function
def Filter(f,R,C):                     # Define the Filter function that corresponds to the low pass RC filter.
    omega = 2*np.pi*f
    vout=( 1j*R*C*omega/(1j*R*omega*C+1.))
    return(vout)
f = np.linspace(10,10000,1000) #Frequncy inputs for the mathematical model
#Treating the experimental data
highpass_data=pd.read_csv('high pass filter values.csv',sep=';',decimal=',')
pd.set_option("display.max.columns", None)
highpass_data.head()
print(highpass_data)
highpass_data['Frq']=highpass_data['Frq'].astype(float)
highpass_data['Ch2Mag']=highpass_data['Ch2Mag'].astype(float)
highpass_data['Ch2Phase']=highpass_data['Ch2Phase'].astype(float)
print(type(highpass_data['Frq']))
Frequency=highpass_data['Frq'].to_numpy()
Magnitude=highpass_data['Ch2Mag'].to_numpy()
Phase=highpass_data['Ch2Phase'].to_numpy()
print(type(Frequency))
#Setting the values of the resistor and capacitor
R=2000. # 2kOhm
C=0.1e-6  # 1µF
#Output voltage
vout_c = Filter(f,R,C)
#Calculating and printing the cutoff frequency
F_cut = 1./(2.*np.pi*R*C)
print("========================================")
print("Filter cut off frequency is: {:7.2f} Hz".format(F_cut))
print("========================================")
#Magntiude function
y_db = 20*np.log10(np.abs(vout_c))
#Magnitude plot
plt.figure(figsize=(15,9)) # Make a figure, and make it bigger.
plt.subplot(2,1,1)         # First subplot in the figure with (2 columns, 1 row, 1st subplot)
plt.plot(Frequency,Magnitude,label='Experimental Data',linewidth=3,color='orange') # Experimental data
plt.plot(f,y_db,label='Mathematical Model',linewidth=3,linestyle=':',color='dodgerblue') #The mathematical model
plt.axvline(x=F_cut, color='r', linestyle='dashed', label='Cutoff Frequency') #Plots a vertical line at the cutoff frequency
plt.axhline(y=-3, color='g', linestyle='dashed',label='-3 dB') #Plots a horizontal line at -3dB
plt.title("Magnitude Plot",fontsize=20)
plt.xlabel("f [Hz]",fontsize=20)
plt.ylabel("Magnitude [dB]",fontsize=20)
plt.xscale("log")           # Set x to a log scale
plt.xticks(fontsize=20) #Set fontsize on numbers on the x-axis
plt.yticks(fontsize=20) #Set fontsize on numbers on the y-axis
plt.grid(True)
plt.tight_layout()          # Automatically adjust spacing between the 2 plots so they do not overlap
plt.legend(loc=4,fontsize='x-large')
#Phaseplot
plt.subplot(2,1,2)
plt.plot(Frequency,Phase,label='Experimental Data',linewidth=3,color='orange') # Experimental data
plt.plot(f,np.angle(vout_c,deg=True),label='Mathematical Model',linewidth=3,linestyle=':',color='dodgerblue') #Mathematical model
plt.axvline(x=F_cut, color='r', linestyle='dashed',label='Cutoff Frequency')  #Plots a vertical line at the cutoff frequency
plt.axhline(y=45, color='m', linestyle='dashed',label='45 Deg') #Plots a line at 45 degrees
plt.title("Phase plot",fontsize=20)
plt.xlabel("f [Hz]",fontsize=20)
plt.ylabel("Phase Angle [Deg]",fontsize=20)
plt.xscale("log")
plt.xticks(fontsize=20) #Set fontsize on numbers on the x-axis
plt.yticks(np.arange(0,105,15),fontsize=20) #Set fontsize on numbers on the y-axis
plt.grid(True)
plt.tight_layout()          # Automatically adjust spacing between the 2 plots so they do not overlap
plt.legend(loc=1,fontsize='x-large')
plt.show()


