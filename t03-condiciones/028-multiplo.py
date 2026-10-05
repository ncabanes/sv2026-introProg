# Múltiplo (V1)

# Pide al usuario dos números enteros y dile 
# si el primero es múltiplo del segundo
# (o si no ocurre así).

n1 = int(input("Dime un número: "))
n2 = int(input("Dime un número: "))

if n1 % n2 == 0:
	print("El primero es múltiplo del segundo")
else:
	print("El primero no es múltiplo del segundo")
