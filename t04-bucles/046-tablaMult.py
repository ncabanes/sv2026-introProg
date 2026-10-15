# Crea un programa que muestre la tabla de 
# multiplicar del número que escoja el usuario, 
# usando "for".

numero = int(input("Qué tabla quieres? "))
for i in range(0, 11):
	print(numero,"x", i, "=", numero*i)
