#Algoritmo Semana3_Seleccion_Multiple
import os
i=0
while(i<=0):
    #Mostrar menu
    os.system("cls") #Limpiar pantalla
    print("MENU DE RECOMENDACIONES")
    print("1.Literatura")
    print("2.Cine")
    print("3.Musica")
    print("4.Videojuegos")
    print("5.Salir")
    #Ingresar una opcion
    print("Eliga una opcion: ")
    opcion = int(input())
    #Procesar esa opcion
    if opcion == 1:
        print("Lecturas recomendables:")
        print("+ Esperandolo a Tito y otros cuentos de futbol(Eduardo Sacheri)")
        print("+ El juego de Ender(Orson Scott Card)")
        print("+ El sueño de los heroes(Adolfo Bioy Casares)")
    elif opcion == 2:
        print("Peliculas recomendables")
        print("+ Matrix(1999)")
        print("+ El ultimo samuray(2003)")
        print("+ Cars(2006)")
    elif opcion == 3:
        print("Discos recomendables:")
        print(" + Despedazado por mil partes (La Renga, 1996)")
        print(" + Búfalo (La Mississippi, 2008)")
        print(" + Gaia (Mägo de Oz, 2003)")
    elif opcion == 4:
        print("Videojuegos clásicos recomendables")
        print("+ Dia del tentaculo(LucaArts,1993")
        print("+ Terminal Velocity(Terminal Reality/3D Realms,1995)")
    elif opcion == 5:
        print("GRACIAS,VUELVA PRONTO")
    else:
        print("OPCION NO VALIDA")
    print("Presione enter para continuar")
    input()
    if opcion == 5:
        break