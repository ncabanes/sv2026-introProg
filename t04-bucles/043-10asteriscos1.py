# Crea un programa que escriba 10 asteriscos, usando "for"

# Versión 1, la más natural para nosotros como novatos
for n in range(1, 11):
	print("*")

# Versión 2, más natural para un programador experimentado
# (empezando a contar desde cero)
for n in range(0, 10):
	print("*")

# Versión 3, la más esperable: se puede omitir el 0 inicial
for n in range(10):
	print("*")
