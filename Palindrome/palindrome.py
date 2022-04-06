# Función para saber si una cadena es palíndrome
def palindromo(palabra):
    # Reemplazando los espacios por una cadena vacía y convertiendo a minúscula
    palabra=palabra.replace(' ','').lower()
    
    if palabra[::]==palabra[::-1]:
        return True
    else:
        return False


def run():
    palabra=input("Ingresa una palabra: ")
    es_palindrome = palindromo(palabra)
    
    if es_palindrome:
        print("Es palindrome")
    else:
        print("No es palindrome")

# Punto de entrada programa de phyton
if __name__ == '__main__':
    run()