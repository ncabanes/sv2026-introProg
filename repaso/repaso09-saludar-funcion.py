# 9. Crea una función "saludar_varias_veces(nombre, veces)", que 
# escribirá varias veces "Hola, " seguido del nombre que se le indique 
# como parámetro. El programa de prueba preguntará al usuario su nombre y 
# cuántas veces quiere que le saludes y se apoyará en ese función para 
# hacerlo.

def saludar_varias_veces(nombre, veces):
	for i in range(veces):
		print("Hola,", nombre)	
	
n = input("Dime tu nombre ")
v = int(input("Cuántas veces te saludo? "))
saludar_varias_veces(n, v)

saludar_varias_veces("Alejandro", 3)
