# Escribe un "tablero de ajedrez", que tendrá 8 filas, cada una 
# con 8 columnas, alternando el símbolo "#" y un espacio en blanco. 
# Debes emplear bucles, no pueden ser 8 órdenes "print". En esta 
# versión no definiremos funciones.
# 
#  # # # #
# # # # # 
#  # # # #
# # # # # 
#  # # # #
# # # # # 
#  # # # #
# # # # # 

for fila in range(8):
	if fila % 2 == 0:
		print(4 * "_#")
	else:
		print(4 * "#_")
