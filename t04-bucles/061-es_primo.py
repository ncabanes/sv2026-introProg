# Crea un programa que pida al usuario un número entero
# y responda si es primo o no.
# 
# Pista: un número es primo si tiene exactamente 2 divisores 
# (si sólo es divisible por el 1 y por sí mismo).

numero = int(input("Qué número quieres comprobar? "))
divisores = 0
for i in range(1,numero+1):
	if numero % i  == 0:
		divisores += 1
if divisores == 2:
	print("Es primo")
else:
	print("No es primo")
