# Repaso de bucles

# Muestra los números del 1 al 100, excepto el 13
# En vez del 50, escribe el texto "Cincuenta"

# Versión 3: continue

for i in range(1, 101):
	if i == 13:	
		continue
	elif i == 50:
		print("Cincuenta", end=" ")
	else:
		print(i, end=" ")
