# 8. Pregunta al usuario su nombre y cuántas veces quiere que le 
# saludes, pero esta vez alternarás entre "Hola, nombre" y "¿Qué tal 
# estás?". Por ejemplo, si se llama "Nacho" y dice que lo quiere repetir 
# 5 veces, tu programa escribirá "Hola, Nacho", en la línea siguiente 
# "¿Qué tal estás?", luego otra vez "Hola, Nacho", y así hasta completar 
# 5 líneas (3 "hola" y 2 "qué tal").

nombre = input("Dime tu nombre ")
veces = int(input("Cuántas veces te saludo? "))

for i in range(veces):
	if i % 2 == 0:
		print("Hola,", nombre)
	else:
		print("¿Qué tal estás?")
