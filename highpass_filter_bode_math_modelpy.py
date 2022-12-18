#Computing the bodeplot for the mathematical model of the highpass filter
#Packages
import matplotlib.pyplot as plt
import numpy as np
#Transfer function
def Filter(f,R,C):                     # Define the Filter function that corresponds to the low pass RC filter.
    omega = 2*np.pi*f
    vout=( 1j*R*C*omega/(1j*R*omega*C+1.))
    return(vout)
f = np.linspace(10,10000,1000) #Frequency inputs
#Values of the resistor and the capacitor
R=2000. # 2kOhm
C=0.1e-6  # 1µF
#The output voltage
vout_c = Filter(f,R,C)
#Calculating and printing the cutoff frequency
F_cut = 1./(2.*np.pi*R*C)
print("========================================")
print("Filter cut off frequency is: {:7.2f} Hz".format(F_cut))
print("========================================")
#Magnitude function
y_db = 20*np.log10(np.abs(vout_c))
#Plotting the magntiude plot
plt.figure(figsize=(15,9)) # Make a figure, and make it bigger.
plt.subplot(2,1,1)         # First subplot in the figure with (2 columns, 1 row, 1st subplot)
plt.plot(f,y_db) # Plot the amplitude, the absolute of the complex number
plt.axvline(x=F_cut, color='r', linestyle='dashed') #Plots a vertical line at the cutoff frequency
plt.title("Magnitude Plot", fontsize=20)
plt.xlabel("f [Hz]",fontsize=20)
plt.ylabel("Magnitude [dB]",fontsize=20)
plt.xscale("log")           # Set x to a log scale
plt.xticks(fontsize=20) #Set fontsize on numbers on the x-axis
plt.yticks(fontsize=20) #Set fontsize on numbers on the y-axis
plt.grid(True)
plt.tight_layout()          # Automatically adjust spacing between the 2 plots so they do not overlap
#The phase plot
plt.subplot(2,1,2)
plt.plot(f,np.angle(vout_c,deg=True)) # Plot the amplitude, the absolute of the complex number
plt.axvline(x=F_cut, color='r', linestyle='dashed')#Plots a vertical line at the cutoff frequency
plt.axhline(y=45, color='b', linestyle='dashed') #Plots a horizontal line at 45 degrees
plt.title("Phase plot",fontsize=20)
plt.xlabel("f [Hz]",fontsize=20)
plt.ylabel("Phase Angle [Deg]",fontsize=20)
plt.xscale("log")
plt.xticks(fontsize=20) #Set fontsize on numbers on the x-axis
plt.yticks(np.arange(0,105,15),fontsize=20) #Set fontsize on numbers on the y-axis
plt.grid(True)
plt.tight_layout()          # Automatically adjust spacing between the 2 plots so they do not overlap
plt.show()

