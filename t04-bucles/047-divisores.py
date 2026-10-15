# Crea un programa que muestre los divisores del número que escoja el 
# usuario, usando "for". Por ejemplo, para el número 75, la respuesta 
# debería ser: 1 3 5 15 25 75

numero = int(input("Ver divisores de... "))
for i in range(1,numero+1):
	if numero % i  == 0:
		print(i, end = " ")
