# Tipos de Datos: Clasificación de los datos
import datetime

# Declarar las variables 
nombre = "Karina"
edad = 21
estatura = 1.69
direccion = "Dr.Velasco, col.doctores"
telefono = "5591056746"
estatus = True # True/False
colores_favoritos = ["rosa", "azul", "morado"] #lista o arreglo
fecha_nacimiento = datetime.date(2001, 10, 20)

# SALIDA DE DATOS
print("Nombre: ", type(nombre))
print("Edad: ", type(edad))
print("Estatura: ", type(estatura))
print("Direccion: ", type(direccion))
print("Telefono: ", type(telefono))
print("Estatus: ", type(estatus))
print("Colores Favoritos", type(colores_favoritos))
print("Fecha de Nacimiento: ", fecha_nacimiento ,type(fecha_nacimiento))