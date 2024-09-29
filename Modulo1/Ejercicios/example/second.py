#determinar la fecha de nacimiento de una persona en base a su edad
YEAR_CUERRENT=2024

edad = int(input("Ingrese su edad actual:"))

fecha_nacimiento=YEAR_CUERRENT - edad

#tipos de salida
#1
print("el año de nacimiento es "+ str(fecha_nacimiento)+" con " +str(edad)+" años")
#2
print("el año de nacimiento es {} con {} años".format(fecha_nacimiento,edad))
#3
print(f"el año de nacimiento es {fecha_nacimiento} con {edad} años") #el mas recomendable


