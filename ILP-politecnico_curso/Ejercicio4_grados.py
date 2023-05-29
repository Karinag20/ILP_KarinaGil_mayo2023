# Ejercicio 4_ Grados convertirlos a °C, °F y °K.

grados_celsius= float(input("Ingrese los grados Celsius (°C):"))
grados_kelvin= float(input("Ingrese los grados Kelvin (°K):"))
grados_fahrenheit= float(input("Ingrese los grados Fahrenheit (°F):"))

# PROCESO
kc = round(grados_kelvin - 273.15) # De Kelvin a Celsius
kf = round(((9 * (grados_kelvin - 273.15) / 5) + 32)) # De Kelvin a Fahrenheit

fc = round((5 * (grados_fahrenheit - 32) / 9),2) # De Fahrenheit a Celsius
fk = round((5 * (grados_fahrenheit - 32) / 9) + 273.15,2) # De Fahrenheit a Kelvin

ck = round(grados_celsius + 273.15) # De Celsius a Kelvin
cf = round(((9 * grados_celsius) / 5) + 32) # De Celsius a Fahrenheit 

# SALIDA
print(grados_kelvin,"°K Su conversion quedo en:  ", kc, "°C") 
print(grados_kelvin,"°K Su conversion quedo en:  ", kf, "°F")

print(grados_fahrenheit,"°F Su conversion quedo en:  ", fc,"°C") 
print(grados_fahrenheit,"°F Su conversion quedo en:  ", fk,"°K")

print(grados_celsius,"°C Su conversion quedo en:  ", ck,"°K") 
print(grados_celsius,"°C Su conversion quedo en:  ", cf,"°F")