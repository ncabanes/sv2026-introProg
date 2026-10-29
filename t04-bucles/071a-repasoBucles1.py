# Repaso de bucles

# Muestra los números del 1 al 100, excepto el 13
# En vez del 50, escribe el texto "Cincuenta"

# Versión 1

for i in range(1, 101):
	if i != 13:
		if i == 50:
			print("Cincuenta", end=" ")
		else:
			print(i, end=" ")
