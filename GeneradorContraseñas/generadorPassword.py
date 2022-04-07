# Módulo para generar un número aleatorio
import random
# Módulo para convertir una lista a string
import string

# Función para generar una contraseña
def generar_contrasena():
    # Lista con todos los caracteres posibles para la contraseña con la libreria string
    caracteres = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase
    print(string.ascii_lowercase)
    print(string.digits)
    print(string.punctuation)
    print(string.ascii_uppercase)

    # Generando contraseña
    contrasena=[]
    
    # Generando longitud de la contraseña
    for i in range(15):
        # Obteniendo un caracter aleatorio de la lista CARACTERES
        caracter_random=random.choice(caracteres)
        # Agregar elementos al array de contraseña
        contrasena.append(caracter_random)

    # Convertir lista a string
    # print(contrasena)
    contrasena=''.join(contrasena)
    
    
    return contrasena

def run():
    contrasena= generar_contrasena()
    print('Tu nueva contraseña es: '+ contrasena)


# Punto de entrada programa de python
if __name__ == '__main__':
    run()