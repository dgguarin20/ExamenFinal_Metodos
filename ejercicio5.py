# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 


import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sigma = 10
beta = 2.67
rho = 28

t = 0 
#x = 0.0
#y = 0.0
#z = 0.0

x =1.0
y =1.0
z =1.0

tfinal = 5.0

xguardar = []
yguardar = []
zguardar =[]
tguardar =[]

xguardar.append(x)
yguardar.append(y)
zguardar.append(z)
tguardar.append(t)

i = 0
dt = 0.1
while (t<tfinal):
    
    dx = sigma*(y-x)
    dy = (rho*x)-y-(x*z)
    dz = -(beta*z) +(x*y)
    
    x = x +dx*dt
    y = y +dy*dt
    z = z+ dz*dt
    t = t +dt
    
    print(x)
    print(y)
    print(z)
    
    xguardar.append(x)
    yguardar.append(y)
    zguardar.append(z)
    tguardar.append(t)

plt.figure()
plt.plot(xguardar,yguardar)
plt.savefig('xy.png')
plt.close()

plt.figure()
plt.plot(xguardar,zguardar)
plt.savefig('xz.png');
plt.show()
