# Repaso de bucles

# Muestra los números del 1 al 100, excepto el 13
# En vez del 50, escribe el texto "Cincuenta"

# Versión 4: continue + break (!!!!!)

for i in range(1, 2000):
	if i == 13:	
		continue
	elif i == 50:
		print("Cincuenta", end=" ")
	else:
		print(i, end=" ")

	if i == 100:
		break # !!!!
