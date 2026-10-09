# Dividir dos números
# Aproximación 2: comprobando una vez si el segundo es cero

a = int(input("Dime un número: "))
b = int(input("Dime otro número: "))
if b == 0:
	b = int(input("No debe ser 0. Dime otro número: "))
print("Su división es",a/b)
