#Solucion Mision Kit Seguro
#Autor:Francin Rodriguez J. Fecha 2026/11/14

nombre = input("Nombre:").strip().upper()
kit = input("tipo de kit:").strip().lower()
autorizacion =input ("tiene autorizacion (si/no):").lower().strip() == "si"

try:
   cantidad = int (input("ingrsese la cantidad:"))
except ValueError:
  print("Error, cantidad invalida -1")
  cantidad = -1
try:
    dias = int(input("ingrese dias de prestamo:" ))
except ValueError:
    print("Error, cantidad invalida ")
    dias = -1
    
resultado = ""  
if not nombre or kit == "" or cantidad < 1 or dias < 1:  
    resultado = "registro rechazado : datos invalidos"

elif  autorizacion and cantidad <= 3 and not dias > 7:
      resultado = f"solicitud aprobada para {nombre}: {cantidad} kit(s) de {kit}."
elif cantidad > 3 or dias > 7:
    resultado = "solicitud enviada a revision"
else:
    resultado = "solicitud rechazada"
    
print (resultado)    



