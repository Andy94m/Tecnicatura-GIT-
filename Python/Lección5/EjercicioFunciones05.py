# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celcius a fahrenheit y viceversa
# Ver formulas

# Función que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# Función que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9 # Respetar presedencia

celsius = float(input('Digite un valor de celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')

fahrenheit = float(input('Digite el valor en fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C -> {resultado:.2f}')