#Algoritmo Semana6_Arreglos o arrays
import random
array = []
for i in range(0,10):
    numeros_random = random.randint(1,20)
    array.append(numeros_random)
print("Los elementos del arreglo son:",array)
print("") # se deja una linea en blanco

for i in reversed(array):
    print("El orden inverso es: ",i)