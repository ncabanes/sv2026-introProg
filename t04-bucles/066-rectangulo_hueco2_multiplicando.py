# Muestra un rectángulo hueco de asteriscos, 
# con 5 filas y 10 columnas, multiplicando textos y números.

for fila in range(5):
	if fila == 0 or fila == 4:
		print("M" * 10)
	else:
		print("M" + "·"*8 + "M")
