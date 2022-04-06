def run():
    for contador in range(100):
        # Imprimiento los números pares
        if contador % 2 != 0:
            # Si se se cumple la condición anterior, no se ejecuta lo que haya después del continue
            continue
        print(contador)

    for i in range(10):
        if i == 5:
            break
        print(i)

    texto=input("Ingrese una frase: ")
    for i in texto:
        if i=='o':
            break
        print(i.upper())

# Punto de entrada programa de python
if __name__=='__main__':
    run()