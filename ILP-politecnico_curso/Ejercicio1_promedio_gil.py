# Ejercicio 1_ calificaciones
 
calificacion_1 = float(input("\nEscribe la primera calificacion: "))
calificacion_2 = float(input("Escribe la segunda calificacion: "))
calificacion_3 = float(input("Escribe la tercera calificacion: "))

# PROCESOS
promedio = (calificacion_1 + calificacion_2 + calificacion_3) /3

if (promedio > 6 and promedio <=10): # Entre 6 y 10
    print("Aprobado")
elif (promedio == 6): # Equivalente a 6
    print("Aprobado de pansaso")
elif (promedio >= 0 and promedio <6): # Entre 0 y menor que 6
    print("Reprobado")
elif (promedio < 10 or promedio > 6): # Menor que 0 o mayor que 10
    print("Promedio inválido")

# SALIDA DE DATOS
print("El promedio es: ", round(promedio,2))