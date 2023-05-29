# Ejercicio 7_ Medir el nivel de agua de una cisterna

nivel=float(input("Indique los litros que hay en la cisterna:"))

# PROCESOS
# SALIDA DE DATOS

if nivel<0:
    print("Fuga en cisterna")
elif nivel ==0:
    print("Encender bomba de agua")
elif nivel >0 and nivel<=2:
    print("Acelerar bomba de agua")
elif nivel >2 and nivel<=4:
    print("Bomba trabajando!")
elif nivel >4 and nivel<6:
    print("Desacelerar bomba")
elif nivel ==6:
    print("Apagar Bomba")
elif nivel >6:
    print("Desbordamiento de agua en cisterna")