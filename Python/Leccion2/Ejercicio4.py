#Ejercicio Etapas de vida según la edad
edad = int (input('Digite su edad: '))
mensaje = None
if 0 <= edad < 10:
    mensaje = 'juego, descrubrimientos: El mundo'
elif 10 <= edad < 20:
    mensaje = 'muchos cambios, mucho que estudiar y potenciar'
elif 20 <= edad < 30:
    mensaje= 'amor y comienza el trabajo'
elif 30 <= edad < 40:
    mensaje= 'trabajo pero un viajecito no viene mal, no? Dos... Tal vez?'
elif 40 <= edad < 60:
    mensaje= 'que disfrutar de lo trabajado'
elif 60 <= edad < 80:
    mensaje= 'descanso, experiencia y sabiduria'
else:
    mensaje = 'Error, etapa de vida no reconocida'
print(f'En los {edad} tenés {mensaje} ')