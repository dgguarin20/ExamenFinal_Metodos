#Ejercicio4
# 'y' es una senal en funcion del tiempo 't' con las unidades descritas en el codigo.
# a. Grafique la senal en funcion del tiempo en la figura 'senal.png' ('y' vs. 't')
# b. Calule la transformada de Fourier (sin utilizar funciones de fast fourier transform) y
# grafique la norma de la transformada en funcion de la frecuencia (figura 'fourier.png')
# c. Lleve a cero los coeficientes de Fourier con frecuencias mayores que 10000 Hz y calcule 
# la transformada inversa para graficar la nueva senal (figura 'filtro.png')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

n = 512 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 128 ) #128 samples per frequency
t = np.linspace( 0, (n-1)*dt, n) 
y = np.sin(2 * np.pi * f * t) + np.cos(2 * np.pi * f * t * t)
noise = 1.4*(np.random.rand(n)+0.7)
y  =  y + noise

#a
plt.plot(y,t)
#b se que era algo asi pero no me acuerdo muy bien x x G(n/N) = sumatoria de 0 a N-1 de fx*e^((n/N)*2*pi*i)
fourier = []
for i in range(0,len(t)):
    valor = 0
    for j in range(0,n-1):
        valor = y[j]*np.exp((t[i]/n)*-2*np.pi*j)+valor
    fourier.append(valor)

#c
timestep = dt
freq = np.fft.fftfreq(n,d=timestep)
print (freq)

for i in range(0,len(fourier)):
    if(freq[i]>10000):
        fourier[i]=0
#d transformada inversa
fourier2 = []
for i in range(0,len(t)):
    valor = 0
    for j in range(0,n-1):
        valor = fourier[j]*np.exp((t[i]/n)*2*np.pi*-j)+valor
    fourier2.append(valor)

plt.plot(t,fourier2)
plt.savefig('filtro.png')

