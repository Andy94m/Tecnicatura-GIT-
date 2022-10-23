class Persona2:
    def __init__(self, nombre, apellido, edad): #encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property #Decorador
    def nombre(self): # Método Getter
        print('Estamos usando el metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre): #Metodo Setter
        #print('estamos utilizando el metodo set')
        self._nombre = nombre

    @property
    def apellido(self, apellido):
        self._apellido = apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self,edad):
        self._edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')


if __name__ == '__main__':
    persona1 = Persona2('Ariel', 'Betancud', 41)
    print(persona1.nombre)  #Llamamos al metodo getter
    persona1.nombre = 'Juan Pedro'
    print(persona1.nombre) #otra vez con el metodo getter
    print(persona1.mostrar_detalles()) #Llamamos el metodo mostrar detalles
    # artibuto read-only (solo lectura seria la edad porque no tiene el metodo set
    print(persona1.edad)

    #Tarea crear tres objetos mas utilizando los metodos getter and setter
    #para modificar y mostrar los cambios

    #tarea objeto1
    persona2 = Persona2('Flor', 'Romero', 23)
    persona2.nombre = 'Florencia'
    persona2.apellido = 'Romery'
    persona2.edad = 22
    print(persona2.mostrar_detalles())

    #tarea objeto2
    persona3 = Persona2('Cari', 'Felisa', 21)
    persona3.nombre = 'Carolina'
    persona3.apellido = 'Felix'
    persona3.edad = 31
    print(persona3.mostrar_detalles())

    #Tarea objeto3
    persona4 = Persona2('Naty', 'Lucer', 35)
    persona4.nombre = 'Natalia'
    persona4.apellido = 'Lucero'
    persona4.edad = 33
    print(persona4.mostrar_detalles())

    print(__name__)

