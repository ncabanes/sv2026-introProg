# Crea una función "escribir_tablero_ajedrez(filas, columnas)", 
# que dibujará un tablero con tantas filas y columnas como 
# indiquen los parámetros, alternando el símbolo "#" y un espacio
# en blanco. Haz un programa de prueba, que pida al usuario el 
# tamaño de ese tablero de ajedrez.
# 
# Versión correcta (uno de los planteamientos posibles): se comporta
# bien si las columnas son impares

def escribir_tablero_ajedrez(filas, columnas):
	for fila in range(filas):
		if fila % 2 == 0:
			print(columnas//2 * ".#", end="")
			if columnas % 2 == 1:
				print(".")
			else:
				print()
		else:
			print(columnas//2 * "#.", end="")
			if columnas % 2 == 1:
				print("#")
			else:
				print()

escribir_tablero_ajedrez(8,8)
print()
escribir_tablero_ajedrez(5,3)
