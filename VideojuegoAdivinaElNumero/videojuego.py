# Módulo para generar un número aleatorio
import random

def run():
    # Generando número aleatorio entre 1 y 10
    numero_aleatorio=random.randint(1,20)
    # Pedir al usuario que ingrese un número
    numero_usuario=int(input("Ingrese un numero del 1 al 20: "))
    # Cantidad de vidas usuario
    vidas=5

    # Mientras el número ingresado sea diferente al número aleatorio
    while numero_usuario!=numero_aleatorio:
        if(numero_usuario<numero_aleatorio):
            print("Elige un numero mas grande")
            vidas-=1
        elif (numero_usuario>numero_aleatorio):
            print("Elige un numero mas pequeño")
            vidas-=1

        if(vidas==0):
            print("Perdiste, el numero era:", numero_aleatorio)
            # Break para salir del ciclo while
            break

        print("Tienes",vidas,"vidas")
        numero_usuario = int(input("Introduce otro número numero: "))
   
    print("FELICIDADES, HAS GANADO")


# Punto de entrada programa de python
if __name__=='__main__':
    run()