# Crea un programa que pida al usuario dos números enteros 
# y muestre sus divisores comunes.

# Versión 1: llegando hasta el primero de los números
# (que quizá sea el mayor, así que puede ser lento)

n1 = int(input("Primer número "))
n2 = int(input("Segundo número "))
for i in range(1,n1+1):
	if n1 % i  == 0 and n2 % i  == 0:
		print(i, end = " ")
