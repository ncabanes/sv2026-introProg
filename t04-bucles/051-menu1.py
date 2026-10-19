# Muestra un menú y di al usuario qué opción ha escogido, hasta que elija salir
# 
# 1. Añadir
# 2. Ver todos
# 0. Salir
# Opción? 2
# Has elegido Ver todos
# 
# 1. Añadir
# 2. Ver todos
# 0. Salir
# Opción? 1
# Has elegido Añadir
# 
# 1. Añadir
# 2. Ver todos
# 0. Salir
# Opción? 0
# ¡Hasta luego!

print("1. Añadir")
print("2. Ver todos")
print("0. Salir")
opcion = input("Elige una opción: ")
while opcion != "0":
	if opcion == "1":
		print("Has elegido Añadir")
	elif opcion == "2":
		print("Has elegido Ver todos")
	else:
		print("Opción incorrecta")

	print()
	print("1. Añadir")
	print("2. Ver todos")
	print("0. Salir")	
	opcion = input("Elige una opción: ")

print("¡Hasta luego!")
