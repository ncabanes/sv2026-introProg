# Pide números al usuario y muestra la media de todos ellos:
# 
# Dime un número (0 para terminar): 20
# La media hasta ahora es 20
# Dime un número (0 para terminar): 10
# La media hasta ahora es 15
# Dime un número (0 para terminar): 0
# ¡ Hasta luego !

suma = 0
cantidad = 0
n = int(input("Dime un número (0 para terminar): "))
while n != 0:
	cantidad += 1
	suma += n
	print("La media hasta ahora es",suma/cantidad)
	n = int(input("Dime un número (0 para terminar): "))
print("¡ Hasta luego !")
