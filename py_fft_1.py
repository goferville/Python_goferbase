import numpy as np
from numpy import fft
import matplotlib.pyplot as plt

n=1000 # Number of data points
dx=5.0 # sampling period, in meters (or any unit)
x=dx*np.arange(0,n) # x coordinates
w1=200 #wave length 1, in meters (or any unit)
w2=20  #wave length 2, in meters (or any unit)
fx=np.sin(2*np.pi*x/w1)+2*np.sin(2*np.pi*x/w2) #signal 1
Fk=fft.fft(fx)/n # Fourier coefficients (divided by n)
nu=fft.fftfreq(n,dx) #Natural frequencies
Fk=fft.fftshift(Fk) #Shift zero frequency to center
nu=fft.fftshift(nu)
fig,ax=plt.subplots(3,1,sharex=True)
ax[0].plot(nu, np.real(Fk))
ax[1].plot(nu, np.imag(Fk))
ax[2].plot(nu, np.absolute(Fk))
plt.show()