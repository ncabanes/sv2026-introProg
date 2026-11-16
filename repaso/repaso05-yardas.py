# 5. Pregunta al usuario una cantidad de yardas y muestra su 
# equivalencia en metros (1 yarda son 0,9144 metros). Si introduce un 
# dato negativo, el programa se debe repetir hasta que introduzca 0 o un 
# valor superior.

yardas = float(input("¿Cuantas yardas? "))
while yardas < 0:
	print("No debe ser negativo")
	yardas = float(input("¿Cuantas yardas? "))

metros = yardas * 0.9144
print("Son",metros,"metros")
