nombre=input("Cual es tu nombre?:")

# Transforma texto a mayúsculas
mayuscula = nombre.upper()
# Transforma texto a la primera en mayúsculas resto en minúsculas
capitalize = nombre.capitalize()
# Elimina espacios en blanco al inicio y al final de la cadena
trim = nombre.strip()
# Transforma texto a minúsculas
minuscula = nombre.lower()
# Remplazando una cadena por otra (a por la e)
reemplazar = nombre.replace("a","e")
# Buscando en que posición se encuentra una cadena
buscar = nombre.find("a")
# Cantidad de caracteres que tiene la cadena
cantidad = len("Hola mundo!")

print(mayuscula)
print(capitalize)
print(trim)
print(minuscula)
print(reemplazar)
print(buscar)
print(cantidad)

# Slices
print(nombre[0])
print(nombre[1])
# 0 al 3 caracter
print(nombre[0:3])
# hasta el 3 caracter
print(nombre[:3])
# 3 al final
print(nombre[3:])
# 1 en 1
print(nombre[::])
# 1 hasta el final de 3 en 3
print(nombre[1::3])
# 1 al 7 de 2 en 2
print(nombre[1:7:2])
# 1 hasta el final pero en pasos negativos (Final a principio)
print(nombre[::-1])
