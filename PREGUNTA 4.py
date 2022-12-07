#Algoritmo Semana5_Metodos

#Funcion que no recibe ni devuelve nada
import os
os.system("cls")
def Saludar():
    return "Hola Mundo!"

#Funcion que recibe un argumento por valor y
#devuelve su doble

num = int(input("Ingrese un numero: "))

def CalcularDoble(num):
    Doble = num * 2 
    return Doble

#Funcion que recibe un argumento por referencia
#y lo modifica

def CalcularTriple(num):
    Triple = num * 3
    return Triple

#Proceso principal que invoca a las funciones
#antes declaradas
print(Saludar())
print("El doble es: ",CalcularDoble(num))
print("El triple es: ",CalcularTriple(num))