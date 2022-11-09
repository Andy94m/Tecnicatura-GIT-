
'''
Definir una clase padre llamada vehiculo y dos clases hijas llamadas auto y bicicleta, las cuales
heredan de la clase padre Vehiculo. La clase padre debe tener los siguientes atributos y metodos:
La clase padre debe tener los siguientes atributos y metodos:

vehiculo(clase padre)
-atributos(color, ruedas)
-metodos (__init__() y __str__() )

auto(clase hija de vehiculo)
-atributos(velocidad (km/hr))
-metodos(__init__() y __str__() )

bicicleta(clase hija de vehiculo)
-atributos (tipo(urbana/montaña/etc)
-metodos(__init__() y __str__()

crear un objeto de cada clase
'''

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: '+self.color+' Ruedas: '+ str(self.ruedas)

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+', Velocidad(Km/hr): '+str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__()+ ', Tipo: '+self.tipo

#Primer objeto de la clase padre Vehiculo
vehiculo = Vehiculo('Blanco', 4)
print(vehiculo)

#Segundo objeto pero ahora de la clase auto
auto = Auto('Amarillo', 4, 120)
print(auto)

# tercer objeto clase bicicleta
bici = Bicicleta('Azul', 2, 'Urbana')
print(bici)

