# Cantidad de pares

# Pide al usuario dos números enteros y respóndele 
# cuántos de ellos son pares ("los dos son pares", 
# "sólo uno es par" o "ninguno es par").

a = int(input("Dime el primero "))
b = int(input("Dime el segundo "))

if (a%2 == 0) and (b%2 == 0):
	print("Los dos son pares")
elif (a%2 == 0) or (b%2 == 0):
	print("Sólo uno es par")
else: 
	print("Ninguno es par")
