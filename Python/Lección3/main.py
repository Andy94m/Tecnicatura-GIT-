'''
#Ciclo while
contador = 0
condicion = True
while contador < 20:
    print(f'Ejecutamos el ciclo while {contador} ')
    contador += 1
else:
    print('Fin del ciclo while')

#imprimir números del 0 al 5 con el ciclo whiiile
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1

minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1

#Ciclo for
cadena = 'Hello'
for letra in cadena:
    print(letra)
else:
    print('Fin del ciclo for')

#Palabra reservada break
for letra in 'Alemania':
    if letra == 'a':
        print((f'letra encontrada: {letra}'))
        break
else:
    print('Fin del ciclo for') '''


#Palabra reservada continue
for i in range(6):
    if i % 2 == 0:
        print(f' valor: {i}')

for i in range (6):
    if i % 2 != 0:
        continue
    print(f'Valor : {i}')

