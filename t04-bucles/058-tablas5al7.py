# Ejercicio 58. Varias tablas de multiplicar
# Muestra las tablas del 5 al 7

for numero in range(5, 8):
	for i in range(0, 11):
		print(numero,"x", i, "=", numero*i)
	print()
