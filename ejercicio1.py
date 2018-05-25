# Ejercicio1
# A partir de los arrays x y fx calcule la segunda derivada de fx con respecto a x. 
# Esto lo debe hacer sin usar ciclos 'for' ni 'while'.
# Guarde esta segunda derivada en funcion de x en una grafica llamada 'segunda.png'

import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = np.linspace(0,2.,10)
fx = np.array([0., 0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.])

derivada = []
x2 =[]

h = fx[1]-fx[0]
valor = fx[0]-2*fx[1]+fx[2]
valor = valor/(h*h)

derivada.append(valor)
x2.append(x[1])
h = fx[2]-fx[1]
valor = fx[1]-2*fx[2]+fx[3]
valor = valor/(h*h)

derivada.append(valor)
x2.append(x[2])

h = fx[3]-fx[4]
valor = fx[2]-2*fx[3]+fx[4]
valor = valor/(h*h)

derivada.append(valor)
x2.append(x[3])

h = fx[4]-fx[5]
valor = fx[3]-2*fx[4]+fx[5]
valor = valor/(h*h)

derivada.append(valor)
x2.append(x[4])

h = fx[5]-fx[6]
valor = fx[4]-2*fx[5]+fx[6]
valor = valor/(h*h)

derivada.append(valor)
x2.append(x[5])

h = fx[6]-fx[7]
valor = fx[5]-2*fx[6]+fx[7]
valor = valor/(h*h)

derivada.append(valor)
x2.append(x[6])

h = fx[7]-fx[8]
valor = fx[6]-2*fx[7]+fx[8]
valor = valor/(h*h)

derivada.append(valor)
x2.append(x[7])

h = fx[8]-fx[9]
valor = fx[7]-2*fx[8]+fx[9]
valor = valor/(h*h)

derivada.append(valor)
x2.append(x[8])


plt.plot(x2, derivada)
plt.show()
plt.savefig('segunda.png')
