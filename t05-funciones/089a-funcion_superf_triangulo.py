# Crea una función "superficie_triangulo", que devuelva su superficie 
# a partir de su base y su altura. Pruébala en un programa.

def superficie_triangulo(b: float, h: float) -> float:
	return b * h / 2

altura = float(input("Altura? "))
base = float(input("Base? "))
print("La superficie es", 
	superficie_triangulo(base, altura))
