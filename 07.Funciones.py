# Creando funciones
def imprimirMensaje():
    print('¡Estoy usando funciones!')
    print('Mensaje especial')

imprimirMensaje()    
imprimirMensaje()
imprimirMensaje()

# Funcione con parametros
def conversacion(mensaje):
    print('Hola')
    print('Cómo estás')
    print(mensaje)
    print('Adios')

opcion=input("Ingrese una opcion (1, 2, 3): ")

if opcion == '1':
    conversacion('Elegiste la opción 1')
elif opcion == '2':
    conversacion('Elegiste la opción 2')
elif opcion == '3':
    conversacion('Elegiste la opción 3')
else:
    print('Opción no válida')
