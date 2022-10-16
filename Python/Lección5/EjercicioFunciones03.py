#Ejercicio 3: Función Recursiva
# Imprimir números de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemeplo si pasamos el valor de 5 debe imprimir:
# 5, 4, 3, etc.
# Si el valor es negativo no devolver nada

def imprimir_numeros_recursivos(numero):
    if numero >= 1:
        print(numero)
        imprimir_numeros_recursivos(numero-1)
    elif numero <= 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorrecto...')
ingreso = int(input('Ingrese su numero mayor a 0: '))
imprimir_numeros_recursivos(ingreso)