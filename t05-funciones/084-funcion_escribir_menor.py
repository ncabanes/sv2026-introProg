# Crea una función "escribir_menor", que reciba 
# dos números como parámetros y escriba en 
# pantalla el valor del menor de los dos:
# 
# escribir_menor(7,5)
# 
# 5

def escribir_menor(n1: float, n2: float) -> None:
	if n1 < n2:
		print(n1)
	else:
		print(n2)
	

escribir_menor(5, 7)
escribir_menor(8, 6)
escribir_menor(4, 4)

