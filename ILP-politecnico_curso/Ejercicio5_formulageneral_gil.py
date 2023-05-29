# Ejercicio 5_ Formula General
import math

a = int (input ("Ingrese el valor de A: "))
b = int (input ("Ingrese el valor de B: "))
c = int (input ("Ingrese el valor de C: ")) 

# PROCESOS

x1 = round(-b-(math.sqrt(b**2)-(4*a*c)))/(2*a)
x2 = round(-b+(math.sqrt(b**2)-(4*a*c)))/(2*a)

# SALIDA DE DATOS
print("Resultado de x1 es: ",x1)
print("Resultado de x2 es: ",x2)