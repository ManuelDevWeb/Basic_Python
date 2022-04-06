# Función para determinar si un número es primo
from copyreg import constructor


def es_primo(numero):
    if numero == 1:
        return False
    else:
        contador=0

    # Recorriendo todos los números del 1 al numero ingresado
    for i in range(1,numero+1):
        # Si esta condición no estuviera, siempre el módulo del segundo if sería 0 (Ya sabemos que al dividir por 1 o por el mismo número, el módulo sería 0)
        if i == 1 or i == numero:                      
            # Si se se cumple la condición anterior, no se ejecuta lo que haya después del continue
            continue
               
        if numero % i == 0:            
            contador += 1
      
        
    if contador == 0:
        return True
    else:
        return False


def run():
    numero=int(input("Ingrese un numero: "))
    if es_primo(numero):
        print("El numero es primo")
    else:
        print("El numero no es primo")

# Punto de entrada programa de python
if __name__=='__main__':
    run()