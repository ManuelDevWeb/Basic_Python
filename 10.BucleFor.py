def run():
    # Imprime los numeros del 1 al 100
    for contador in range(1, 101):
        print(contador)

    # Imprime los numeros del 1 al 100, pero de 2 en 2
    for i in range(0, 101, 10):
        print(i)

    # Imprimiento los numeros del 1 al 10 y multiplicando por 10
    for i in range(1, 11):
        print(i*10)

    # Pidiendo el nombre al usuario
    nombre=input("Ingrese su nombre: ")
    # Pidiendo frase al usuario
    frase=input("Ingrese una frase: ")

    # Recorriendo la cadena
    for i in nombre:
        print(i)

    # Recorriendo la cadena
    for i in frase:
        print(i.upper())

# Punto de entrada programa de python
if __name__=='__main__':
    run()