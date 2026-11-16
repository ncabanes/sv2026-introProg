# 7. Pregunta al usuario su nombre y 
# cuántas veces quiere que le saludes. 
# Por ejemplo, si se llama "Nacho" y 
# dice que lo quiere repetir 5 veces, 
# tu programa escribirá 5 líneas 
# "Hola, Nacho".

nombre = input("Dime tu nombre ")
veces = int(input("Cuántas veces te saludo? "))

for i in range(veces):
	print("Hola,", nombre)
