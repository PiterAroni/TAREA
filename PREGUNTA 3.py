#Algoritmo Semana4_For

#Calcula el promedio de una lista de N datos
import os
os.system("cls")
print("Ingrese la cantidad de datos: ")
n_datos = int(input())

acum = 0

for i in range(n_datos):
    print("Ingrese el dato ",i,":")
    dato = int(input())
    acum = acum + dato

prom = acum/n_datos
print("El promedio es: ",prom)
