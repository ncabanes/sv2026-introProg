# Crea una función "dibujar_rectangulo_hueco", 
# que dibuje un rectángulo hueco (sólo borde, 
# no relleno) con el ancho, alto y símbolo que 
# se indiquen como parámetro. Si no se detalla 
# el símbolo, se usarán asteriscos.

def dibujar_rectangulo_hueco( ancho: int,
		alto: int, simbolo: str = "*") -> None:
			
	# Primera línea
	print(ancho * simbolo)
	
	# Líneas intermedias
	for fila in range(alto-2):
		print(simbolo + (ancho-2) * " " + simbolo) 
		
	# Última línea
	print(ancho * simbolo)

dibujar_rectangulo_hueco(20, 10, "#")
print()   # Línea en blanco para separar
dibujar_rectangulo_hueco(10, 5)
