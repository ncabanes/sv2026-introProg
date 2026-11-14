# Volumen de una piramide

# Crea una función "volumen_piramide", que devuelva el volumen 
# de una pirámide de base rectangular, a partir los dos lados
# de la base y su altura (volumen = a · b · h / 3).

def volumen_piramide(lado1: float,
		lado2: float, altura: float) -> float:
	return lado1 * lado2 * altura / 3

a = float(input("Dime un lado de la base: "))
b = float(input("Dime el otro lado de la base: "))
h = float(input("Dime la altura: "))

v = volumen_piramide(a,b,h)
print("El volumen es", v)
