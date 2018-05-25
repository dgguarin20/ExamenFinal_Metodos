#Ejercicio3
# Los arrays `u` y `v` representan dos series en funcion del tiempo `t`.
# Grafique las dos series de datos en una misma imagen 'serie.png'
# Calcule la covarianza entre `u` y `v` e imprima su valor.

import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


t = np.array([0.,0.1,0.2,0.3,0.4,0.5,0.6, 0.8, 0.9])
u = np.array([12.,45.,6.,78.,34.,22.,-10.,31.,-27.])
v = np.array([3.,11.,1.3,37.,11.,6.,-23.,7.,7.])


plt.plot(t,u)
#hold on
plt.plot(t,v)

plt.show()
plt.savefig('serie.png')

cov = []
mediaU = 0;
mediaV =0;
for i in range(0,len(t)):
    mediaU = mediaU + u[i]
    mediaV = mediaV + v[i]

mediaU = mediaU/len(t)
mediaV = mediaV/(len(t))
N = len(t)
for i in range(0,len(t)):
    res = ((u[i]-mediaU)*(v[i]-mediaV))/(N-1)
    cov.append(res)

print(cov)    
    