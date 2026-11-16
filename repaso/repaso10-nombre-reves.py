# 10. Se puede saber la longitud de un texto con len(texto). Por 
# ejemplo, len("Hola") vale 4. Además, podemos saber la letra que hay en 
# una cierta posición usando "corchetes". Por ejemplo, si hacemos 
# saludo="Hola", el valor de saludo[1] será la letra "o". Crea un 
# programa que pida al usuario su nombre y lo muestre al revés usando len 
# y [].

nombre = input("Dime tu nombre ")
longitud = len(nombre)

# Acercamiento: espacios intermedios
for i in range(longitud):
	print(nombre[i], end=" ")

# Línea en blanco para poder comprobar
print()

# Lo que me piden: al revés (desde longitud-1, hasta 0 -incluido-)
for i in range(longitud-1, -1, -1):
	print(nombre[i], end="")
