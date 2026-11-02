# Escribir descendente, desde un cierto número hasta 0

# Crea una función "escribir_descendente", que escriba 
# desde un cierto número hasta 0, descendiendo, en la 
# misma línea, separados por un espacio.

def escribir_descendente(n : int) -> None:
	for i in range(n, 0, -1):
		print(i, end=" ")

escribir_descendente(10)
