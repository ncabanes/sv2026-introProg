# Pide números al usuario y muestra la suma de todos ellos:
# 
# Dime un número (0 para terminar): 20
# La suma hasta ahora es 20
# Dime un número (0 para terminar): 15
# La suma hasta ahora es 35
# Dime un número (0 para terminar): -7
# La suma hasta ahora es 28
# Dime un número (0 para terminar): 0
# ¡ Hasta luego !

suma = 0
n = int(input("Dime un número (0 para terminar): "))
while n != 0:
	suma += n
	print("La suma hasta ahora es",suma)
	n = int(input("Dime un número (0 para terminar): "))
print("¡ Hasta luego !")
