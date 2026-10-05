# Múltiplo (V2)

# Pide al usuario dos números enteros y dile si
# alguno de ellos es múltiplo del otro 
# (o si no ocurre así).

a = int(input("Dime un número "))
b = int(input("Dime otro número "))
if (a % b == 0) or (b % a == 0):
	print("Alguno es múltiplo del otro")
else:
	print("Ninguno es múltiplo del otro")
