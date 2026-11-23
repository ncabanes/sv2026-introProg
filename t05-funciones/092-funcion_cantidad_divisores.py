# 2. Crea una función "cantidad_divisores", 
# que devuelva la cantidad de divisores del 
# número que se indique como parámetro.

def cantidad_divisores(numero: int) -> int:
	cantidad = 0
	for divisor in range(1, numero+1):
		if numero % divisor == 0:
			cantidad += 1
	return cantidad

if cantidad_divisores(6) != 4:
	print("Mal")
else:
	print("Empezamos bien")
