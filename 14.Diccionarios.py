# Diccionarios: Son una estructura de datos mutable las cuales almacenan diferentes 
# tipos de valores sin darle importancia a su orden. Identifican a cada elemento por 
# una clave (Key). Se escriben entre {}.

# Operaciones:

# • .keys() —> Retorna la clave de nuestro elemento

# • .values()—> Retorna una lista de elementos (valores del diccionario)

# • .items() —> Devuelve lista de tuplas (primero la clave y luego el valor)

# • .clear() —> Elimina todos los items del diccionario

# • .pop(“n”) —> Elimina el elemento ingresado

def run():
    # Generando diccionarios (Estructura de datos de llaves y valor)
    mi_diccionario={
        'nombre':'Manuel',
        'apellido':'Valencia',
        'edad': 21,
        'trabaja': True,
        'cursos': ['Python','Java','C#']
    }

    print(mi_diccionario)
    # Accediendo a los valores de un diccionario
    print(mi_diccionario['nombre'])
    print(mi_diccionario['apellido'])
    print(mi_diccionario['edad'])
    print(mi_diccionario['trabaja'])

    # Modificando valores de un diccionario
    mi_diccionario['cursos'].append('PHP')
    print(mi_diccionario['cursos'])

    mi_diccionario.pop('trabaja');
    print(mi_diccionario)

    # Diccionario de poblaciones
    poblacion_paises={
        'Mexico':12_000_000,
        'Colombia':11_000_000,
        'Argentina':4_000_000,
        'Venezuela':21_000_000
    }

    # Imprimiento llaves de un diccionario
    for pais in poblacion_paises.keys():
        print(pais)

    # Imprimiento valores de un diccionario
    for poblacion in poblacion_paises.values():
        print(poblacion)

    # Imprimiento items de un diccionario
    for poblacion_pais in poblacion_paises.items():
        print(poblacion_pais)

    for pais in poblacion_paises:
        print(pais,'tiene',poblacion_paises[pais],'habitantes')

    

# Punto de entrada programa de python
if __name__=='__main__':
    run()