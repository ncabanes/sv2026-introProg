# Triángulo del tamaño que elija el usuario

# *****
# ****
# ***
# **
# *

tamanyo = int(input("Tamaño? "))
ancho = tamanyo
for fila in range(tamanyo):
	for columna in range(ancho):
		print("*", end = "")
	print()
	ancho -= 1

