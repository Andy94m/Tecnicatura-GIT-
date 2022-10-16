# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
# numéricos, utilizando argumentos variables *args como parametro de la
# función y agregar como resultado de la suma de todos los valores pasados
# como argumentos.
# definimos la función

def sumar_valor(*args): #recibimos una cantidad de parámetros indefinidos
    resultado = 0
    #iteramos cada elemento
    for valor in args:
        resultado += valor
    return resultado


# Llamamos a la funcion
print(sumar_valor(3, 5, 9))

