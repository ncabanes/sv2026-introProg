# 4. Pide al usuario que introduzca un 
# número real mayor que 10. El programa 
# debe repetirse hasta que lo haga 
# correctamente.

a = float(input("Dime un número: "))
while a <= 10:
	print("Debe ser mayor de 10")
	a = float(input("Dime un número: "))

print("Ok")
