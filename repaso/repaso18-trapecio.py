# Escribe un programa que pida un ancho (de la base mayor) y un alto, así 
# como un carácter, y muestre un trapecio de tamaño descendente como 
# éste:
# 
# Introduzca el ancho mayor deseado: 9
# Introduzca el alto deseado: 3
# Introduzca el carácter: *
# 
# *********
#  *******
#   *****

ancho = int(input("Introduzca el ancho mayor deseado: "))
alto = int(input("Introduzca el alto deseado: "))
caracter = input("Introduzca el carácter: ")

espacios = 0
for fila in range(alto):
	print(" " * espacios, end="")
	print(caracter * ancho)	
	ancho -= 2
	espacios += 1
