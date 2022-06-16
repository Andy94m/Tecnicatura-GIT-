'''
#En esta clase veremos la sentencia if/else
condicion = 'hola'
if condicion == True:
    print('Condicion Verdadera')
elif condicion == False:
    print('Condicion Falsa')
else:
    print('Condicion sin especificar') '''

# Conversion de numero a texto
# num = int(input('Digite un numero en el rango del 1 al 3: '))
# numTexto = ''
# if num == 1:
#     numTexto = 'Numero uno'
# elif num == 2:
#     numTexto = 'Número dos'
# elif num == 3:
#     numTexto = 'Número tres'
# else:
#     numTexto = 'Has ingresado un número fuera del rango'
#
# print(f'El número ingresado es: {num} - {numTexto}')


#Classic if
condicion = False
# if condicion:
#     print('Condicion Verdadera')
# else:
#     print('Condicon Falsa')

#Operador ternario simplificado, solo se recomienda si es codigo pequeño
print ('Condicion Verdadera') if condicion else print ('Condicion Falsa')

