# Listas de números
numeros=[1,2,3,4,5,6,7,8,9,10]
objetos=['Hola',3.5,4.5,True]

print(numeros)
print(objetos)

# Acceder a un elemento de un array
print(numeros[1])

# Agregar elementos al array
numeros.append(11)
print(numeros)

# Eliminar elementos del array (Enviamos indice)
# numeros.pop(1)
print(numeros)

# Recorrer array
for numero in numeros:
    print(numero)

# Podemos implementar algunos métodos de strings
# Recorrer hasta el elemento 3
print(numeros[:3])

# Recorrer desde el elemento 3 hasta el final
print(numeros[3:])

# 1 hasta el final pero en pasos negativos (Final a principio)
print(numeros[::-1])

# 1 al 7 de 2 en 2
print(numeros[0:1])
