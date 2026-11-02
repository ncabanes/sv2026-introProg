# Crea una función "area_circulo". que devuelva el área de 
# un círculo a partir de su radio, que recibirá como parámetro

def area_circulo(radio: float) -> float:
	return 3.1415926535 * radio * radio

print("El area de un círculo de radio 5 es",
	area_circulo(5))
