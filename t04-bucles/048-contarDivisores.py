# Crea un programa que responda la cantidad de divisores del número que 
# escoja el usuario, usando "for". Por ejemplo, para el número 75, la 
# respuesta debería ser: 6 (porque sus divisores son 1 3 5 15 25 75).

numero = int(input("Cantidad de divisores de... "))
divisores = 0
for i in range(1,numero+1):
	if numero % i  == 0:
		divisores += 1
print("Cantidad de divisores:", divisores)
