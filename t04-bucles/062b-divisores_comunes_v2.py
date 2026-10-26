# Crea un programa que pida al usuario dos números enteros 
# y muestre sus divisores comunes.

# Versión 2: llegando hasta el menor de los números
# (más rápido)

n1 = int(input("Primer número "))
n2 = int(input("Segundo número "))

menor = n1 if n1 < n2 else n2
# if n1 < n2:
# 	menor = n1
# else:
# 	menor = n2

for i in range(1,menor+1):
	if n1 % i  == 0 and n2 % i  == 0:
		print(i, end = " ")
