class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, dni,  edad, *args, **kwargs): # se lo llama init dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): # self es igual a this
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.kwargs}')


persona1 = Persona('Ariel', 'Betancud',12344543 , 40)  # Necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Osvaldo', 'Giordanini', 13, 45)
print(f'El objeto 2 de la clase persona se llama: {persona2.nombre} {persona2.apellido} y su edad es: {persona2.edad}')

persona1 = Persona('Ariel', 'Betancud',23 ,40)
print(f'El objeto 1 de la clase persona se llama: {persona1.nombre} {persona1.apellido} y su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(
    f'El objeto1 modificado de la clase persona es: {persona1.nombre} {persona1.apellido} y su edad es: {persona1.edad}')

# Los atributos son: caracteristicas
# Los métodos son: El compartamiento que van a tener los objetos (acciones)

persona1.mostrar_detalle() # La referencia se pasa de forma automatica
persona2.mostrar_detalle()

#Persona.mostrar_detalle(persona1) # Debe ingresarse algun objeto como referencia

persona1.telefono = '1112312'
print(f' Es es el telefono de: {persona1.nombre} {persona1.telefono}') # Se crea el atributo solo para el objeto1

# print(persona2.telefono) no existe

persona3 = Persona('Rogelio', 'Romero', 35656323, 22, 'Telefono', '123333231', 'Calle Lopez', 876, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='azul', auto='Citroen', Modelo=2021 )
persona3.mostrar_detalle()
#print(persona3._dni) #Esto no se debe utilizar en python(Esta encapsulado), esto dice que lo desconocemos
#persona3.__nombre  # esto es un error
