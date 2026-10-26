# Usando bucles anidados, muestra un rectángulo hueco de asteriscos, 
# con 5 filas y 10 columnas.

for fila in range(5):
	for columna in range(10):
		if fila == 0 or fila == 4 or columna == 0 or columna == 9:
			print("*", end = "")
		else:
			print("·", end = "")
	print()
