'''
miVariable = 3
print (miVariable)
miVariable = "hola k ase"
print(miVariable)
miVariable = 3.5
print(miVariable)

x = 10
y = 2
z = x + y
print(id(x))
# las literales(posiciones de memoria) se escriben x624. con X y los tres ultimos numeros de su posicion


a = "gola mundo"
print (type(a)) #devuelve el tipo de variable

a = False
print (type (a)) #los tipos de datos son CLASES

# manejo de cadenas (String)
miGrupoFavorito = "The Letter Black: "
caracteristicas = "The best rock band"
print ("mi grupo favorito es: ", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(numero1 + numero2)

print(int(numero1) + int(numero2))

#tipos boleanos (bool)
miBooleano = True
print(miBooleano)

miBooleano = 1 > 2
print(miBooleano)

miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("el resultado es verdadero")
else:
    print("el resultado es falso")

#procesar la entrada del usuario
#funcion input

resultado = input ("digite un numero: ") #regresa un dato tipo string
print(resultado)


#conversion de la entrada de datos
numero1 = int (input ("escribe el primer numero: "))
numero2 = int (input ("escribe el segundo numero: "))
resultado = numero1 + numero2
print(resultado) '''

'''
'print comun'
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print ("Resultado de la suma: ", suma)

'print ideal para concatenar correctamente. F de format y se incluyen las variables dentro de la concatenacion'
print (f'El resultado de la suma es: {suma}')

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"el resultado de la multiplicacion es: {multiplicacion}")

division =  operandoA / operandoB
print(f"el resultado de la division es: {division}")

division = operandoA // operandoB
print(f"el resultado de la division (int) es: {division}")

modulo = operandoA % operandoB
print(f"el resultado de la division o residuo (modulo) es: {modulo}") '''

'''
alto = int (input('Proporciiona el alto del rectangulo: '))
ancho = int (input ('proporciona el ancho del rectangulo'))
area = alto * ancho
perimetro = (alto+ ancho) *2
print ('area : ', area)
print ('perimetro : ', perimetro) '''


'''
miVariable3 = 10
print (miVariable3)

#operadores de reasignacion
miVariable3 = miVariable3 +1
print (miVariable3)

#otra sintaxis, tambien se puede hacer con todos los otros operadores aritmeticos
miVariable3 += 1
print(miVariable3) 

#operadores de comparacion

d=7
b=4
resultado = d == b #comprobamos si son iguales
print (resultado)

#operador diferente
resultado = d != b
print(resultado)

#operador mayor que
resultado = d > b
print(resultado) 

a = int (input ("digite un numero: "))
print (f"el residuo de la diivision es: {a % 2}")
if a % 2 == 0:
    print(f"El valor de a es: {a} es un numero PAR")
else:
    print(f"el valor de a es: {a} es un numero IMPAR") 

edadAdulto = 18
edadPersona = int (input("digite su edad: "))
if edadPersona >= edadAdulto:
    print(f"Su edad es: {edadAdulto} es mayor de edad")
else:
    print(f"Su edad es: {edadAdulto} es menor de edad") 


#operador AND
a = False
b = True
resultado = a and b
print (resultado)

#operador OR
resultado = a or b
print(resultado)

#operador NOT
resultado = not a
print(resultado) 

#ejercicio: Valor dentro de un rango
valor = int(input("Digite un numero dentro del rango 0 a 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >=valorMinimo and valor <= valorMaximo) #parentesis opcionales
if dentroRango:
    print(f'El valor {valor} esta dentro del rango')
else:
    print(f'El valor {valor} no esta dentro del rango') 

#Ejercicio con el operador OR. Operador NOT
vacaciones = True
diaDescanso = False
if not (vacaciones or diaDescanso):
    print('Tiene trabajo que hacer')
else:
    print('Puede asistir al juego') 

#Ejercicio: Rango entre 20 y 30 años
#sintaxis simplifcada del operador and
edad = int(input("Digite su edad: "))
if (20 <= edad < 30) or (30 <= edad < 40):
    print("Estas dentro del rango de los (20'0)  a (30'0) años")
else:
    print("No estas dentro del rango de los (20'0)  a (30'0) años") 

#Ejercicio: El mayor de dos NÚMEROS
numero1 = int(input('Digite el valor para el numero1: '))
numero2 = int(input('Digite el valor para el numero2: '))

if numero1 > numero2:
    print('El numero 1 es mayor')
else:
    print('El numero 2 es mayor')  '''

#Ejercicio: Tienda de libros
print('Digite los siguientes datos del libro')
nombre = input('Digite el nombre del libro: ')
id = int(input('Digite el ID del libro: '))
precio = float(input('Digite el precio del libro: '))
envioGratuito = input ('Indicar si el envio es gratuito (True/False): ')
if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'El valor es incorrecto, debe escribir True/False'
print(f'''
    Nombre: {nombre}
    id: {id}
    precio: {precio}
    Envio Gratuito? {envioGratuito}
''')

