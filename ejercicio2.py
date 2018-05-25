# Ejercicio 2
# Complete el siguiente codigo para recorrer la lista `x` e imprima
# los numeros impares y que pare de imprimir al encontrar un numero mayor a 800
import numpy as np

x = np.int_(np.random.random(100)*1000)
s =0
while s< len(x):
    if(x[s]>800):
        s = len(x)+1
    else:
        if(x[s]%2 !=0):
            print(x[s])
    s = s+1
    
        
print(x)



