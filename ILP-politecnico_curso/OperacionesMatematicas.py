# EJEMPLO 2. Operaciones Matematicas:
# Suma, Resta, Mult, Div, Potencia, Raiz, Modulo

# Importar una libreria de funciones matematicas
import math

# ENTRADA DE DATOS
# Declarar o crear las VARIABLES

#numero_1 = 10
#numero_2 = 2
numero_3 = 5.87687

# El ususario ingresa el dato
numero_1 = int(input("Escribe el 1er numero: ")) #convertir mi dato en entero
numero_2 = int(input("Escribe el 2do numero: "))

# PROCESOS (Operaciones o calculo matematicos y/o logicos)
suma = numero_1 + numero_2
resta = numero_1 - numero_2 
multiplicacion = numero_1 * numero_3
division = numero_1 / numero_3

potencia_1 = numero_1 ** numero_2
potencia_2 = pow(numero_1, numero_2)
cuadrado = numero_1 ** 2 
cubo = pow(numero_2, 3)

raiz_cuadrada_1 = math.sqrt(9)
raiz_cuadrada_2 = pow (9, 1/2)
raiz_cubica = pow (27, 1/3)

modulo_residuo = 20%6
 
# SALIDA DE DATOS
print (numero_1 + numero_2) # forma mas larga e innecesario, contamos con variables

# Formas distintas de imprimir 
print ("La suma es = ",suma) # CONCATENACION (Union de 2 o más textos)
print ("La suma es = " + str(suma)) # CONCATENACION (Union de 2 o más textos)
# CASTEO (Convertir un tipo de dato en otro tipo de dato)
print (f"La suma es = {suma}") # CONCATENACION (Union de 2 o más textos)
# Interpolacion de texto f= formatear

print (resta) # Resultado
print ("La multiplicacion es = ",round(multiplicacion,2)) #round funciona para redondear
print ("La division es = ",round(division))

print ("La potencia_1 es = ",potencia_1)
print ("La potencia_2 es = ",potencia_2)
print ("La cuadrado es = ",cuadrado)
print ("La cubo es = ",cubo)

print ("La raiz_cuadrada_1 es = ",raiz_cuadrada_1)
print ("La raiz_cuadrada_2 es = ",raiz_cuadrada_2)
print ("La raiz_cubica es = ",raiz_cubica)

print ("El modulo es = ",modulo_residuo)