# Pregunta al usuario cuántas filas quiere que dibujes en pantalla (por ejemplo, 
# 6). En las filas impares (primera, tercera, etc.) escribirás 8 asteriscos. En 
# las filas pares (segunda, cuarta, etc.) escribirás 8 almohadillas:
# 
# Cuántas filas? 5
# ********
# ########
# ********
# ########
# ********
# 
# Observación: hacerlo sin funciones puntúa sobre 8. Para puntuar sobre 10, se 
# debe definir una función "dibujar_varias_filas(cantidad)" y usarla desde el 
# cuerpo del programa.
# 
# Versión 2: sin función, contando desde 1

filas = int(input("Cuántas filas? "))

for i in range(1, filas+1):
	if i % 2 == 1:
		print(8 * "*")
	else:
		print(8 * "#")
