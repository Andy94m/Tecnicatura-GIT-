# Comenzamos con Funciones
# Definimos una función con def


# Todo codigo que respete el identado será parte de la función
def mi_funcion():
    print('Saludos a todos los alumnos jeje')

mi_funcion() #Ej llamado de función

mi_funcion()
mi_funcion()

# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1]) #Pasamos uno por uno los datos de la lista a la función
show(*person) # Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Osvaldo", "Giordanini") #Desempaquetamos a través de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)

numbers = [1, 2, 3, 4, 5] # Aun con la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break #Esta es la unica manera para que no se ejecute el else
else:
    print('Esto se terminó')

#List comprehension, lista de comprensión
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == 'p'] # Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country" : "Arg" },
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]

#Paso de argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos los que ven a través del canal de Youtube")
    print(f'Nombre: {name}, Apellido: {lastName}')
mi_funcion2('Jorge', 'Lucero')
mi_funcion2('Ariel', 'Betancud')
mi_funcion2('Analia', 'Pedrosa')

#La palabra return en funciones
#Creamos una funcion para sumar
def sumar(a, b):
    return a + b
resultado = sumar(78, 22)
print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')

def sumar2(a = 0, b = 0): #le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

def listarNombres(*nombres): # Normalmente se utiliza: *args
    for nombre in nombres:  # Se va a comvertir en una tupla
        print(nombre)
listarNombres('Lucas', 'José', 'Claudia', 'Rosa', 'Maria')
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')

def listarTerminos(**terminos): #gralmente se usa **kwargs
    for llave, valor, in terminos.items():
        print(f'{llave} : {valor}')

listarTerminos() # No recibe nada, nada se va a mostrar
listarTerminos(IDE='Inetrated Develoment Enviroment', PK='Primary Key')
listarTerminos(Nombre='Leonel Messi')


def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
#desplegarNombres(10, 11) #no es un objeto iterable
desplegarNombres((10, 11)) # La convertimos en tupla
desplegarNombres([22, 55]) # Convertimos en una lista



# Funciones Recursivas
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1) # Caso Recursivo
numeroFactorial = int(input('Digite el numero para calcular el factorial: '))
resultado = factorial(numeroFactorial)
print(f'El factorial del número {numeroFactorial} es: {resultado}')
