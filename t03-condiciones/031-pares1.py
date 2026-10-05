# Pide al usuario dos números enteros pares y respóndele 
# si lo ha hecho bien (porque los dos son pares) o lo ha 
# hecho mal (porque alguno es impar).

print("Dime dos números pares")
a = int(input("Dime el primero "))
b = int(input("Dime el segundo "))

if (a%2 == 0) and (b%2 == 0):
	print("Los dos son pares")
else: 
	print("Alguno es impar")

# Alternativo
if (a%2 != 0) or (b%2 != 0):
	print("Alguno es impar")
else: 
	print("Los dos son pares")
