# Crea una nueva versión del menú, 
# que use un booleano en el "while".

terminado = False
while not terminado: 
	print()
	print("1. Añadir")
	print("2. Ver todos")
	print("0. Salir")	
	opcion = input("Elige una opción: ")	
	
	if opcion == "1":
		print("Has elegido Añadir")
	elif opcion == "2":
		print("Has elegido Ver todos")
	elif opcion == "0":
		terminado = True
	else:
		print("Opción incorrecta")

print("¡Hasta luego!")
