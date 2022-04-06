def run():
    LIMIT = 10
    contador=0
    
    # Bucle while
    while contador < LIMIT:
        # Potencia de 2
        potencia_2=2**contador
        print('2 elevado a '+ str(contador)+' es igual a: '+ str(potencia_2))
        contador+=1
    


# Punto de entrada programa de pyton
if __name__ == '__main__':
    run()