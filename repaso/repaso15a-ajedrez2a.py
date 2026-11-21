# Crea una función "escribir_tablero_ajedrez(filas, columnas)", 
# que dibujará un tablero con tantas filas y columnas como 
# indiquen los parámetros, alternando el símbolo "#" y un espacio
# en blanco. Haz un programa de prueba, que pida al usuario el 
# tamaño de ese tablero de ajedrez.
# 
# Primera aproximación: sólo se comportará correctamente si
# las columnas son pares (si son impares, escribe una de menos)

def escribir_tablero_ajedrez(filas, columnas):
	for fila in range(filas):
		if fila % 2 == 0:
			print(columnas//2 * ".#")
		else:
			print(columnas//2 * "#.")

escribir_tablero_ajedrez(8, 8)

print()
escribir_tablero_ajedrez(16, 10)

print()
escribir_tablero_ajedrez(5, 5)
