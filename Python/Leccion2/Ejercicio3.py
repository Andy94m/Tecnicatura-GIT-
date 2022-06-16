#Ejerciicio calcular la estación del año
mes = int(input('Digite un mes del año (1-12): '))
estacion = None
if mes == 1 or mes == 2 or mes == 3:
    estacion = 'Calor! Pileta! Verano!'
elif mes == 4 or mes == 5 or mes == 6:
    estacion = 'Se caen las ojas, Otoño'
elif mes == 7 or mes == 8 or mes == 9:
    estacion = 'Se prende la estufa... Invierno'
elif mes == 10 or mes == 11 or mes == 12:
    estacion = 'Se alargan los dias, llegó la Primavera!'
else:
    estacion = 'En que planeta vivis? Solo hay 12 meses '
print(f'para el mes {mes} la estacion es: {estacion}')


