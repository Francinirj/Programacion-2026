"""Microreto: el portero del café."""

energia = int(input("cuanta energia tiene de cero a 100?:" ))
trae_cafe = input("¿Traes café? (si/no): ").lower().strip() =="si"

mensaje = "Completa las reglas del portero."

# <30 y no traigo cafe, no se entra
# si traigo 30 o masde energia o tengo cafe dejeme pasar
#portero confundido, revisa las repuestas
if energia < 30 and not (trae_cafe) :
    mensaje = "acceso denegado: necesita dormir o tomar cafe."
elif energia >=30 or trae_cafe:
    mensaje = "acceso permitido: pasa pero comparte el cafe"
else:
    mensaje ="el guarda esta confundido, revisa las respuestas"

# TODO: usa and para detectar energía baja sin café.
# TODO: usa or para permitir energía suficiente o café.
# TODO: escribe mensajes claros para cada resultado
print (mensaje)

