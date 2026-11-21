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
# Versión 4: contando desde 0, con función y anotación de tipos

def escribir_varias_filas(filas: int) -> None:
	for i in range(filas):
		if i % 2 == 0:
			print(8 * "*")
		else:
			print(8 * "#")

filas = int(input("Cuántas filas? "))
escribir_varias_filas(filas)
print()
escribir_varias_filas(3)
