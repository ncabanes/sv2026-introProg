# Dividir dos números
# Forma correcta: el segundo no debe ser cero

a = int(input("Dime un número: "))
b = int(input("Dime otro número: "))
while b == 0:
	b = int(input("No debe ser 0. Dime otro número: "))
print("Su división es",a/b)
