# Función para reutilizar código
def conversor(tipo_peso, valor_dolar):
    # Almacenar cantidad de pesos que ingresa usuario
    pesos=float(input("¿Cuántos pesos " + tipo_peso + " tienes?"))    
    # Calcular la cantidad de dolares
    dolares=pesos/valor_dolar
    # Redondeando el resultado de dolares
    dolares=round(dolares,2)
    # Convirtiendo el resultado de dolares a string
    dolares=str(dolares)
    print("Tienes $" + dolares + " dolares")

# Menú (Cadena de carácteres)
menu="""
    Bienvenido al conversor de monedas 🪙💰

    1. Pesos colombianos
    2. Pesos argentinos
    3. Pesos mexicanos

    Elige una opción: """

# Almacenando la opción del usuario
opcion=input(menu)

# Condicionales
if opcion=="1":
    conversor("colombianos", 3800)
elif opcion=="2":
    conversor("argentinos", 65)
elif opcion=="3":
    conversor("mexicanos", 24)
else:
    print("Opción inválida")



