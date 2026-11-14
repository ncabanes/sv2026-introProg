# Dime un número: 3
# Operación: +
# Dime el otro número: 5
# 3 + 5 = 8

# Esta segunda versión se debe repetir hasta que la operación
# sea la palabra "exit"

n1 = float(input("Dime un número: "))
operacion = input('Operación ("exit" para salir): ')
n2 = float(input("Dime el otro número: "))

while operacion != "exit":

	if operacion == "+":
		print(n1, "+", n2, "=", n1+n2)
	elif operacion == "-":
		print(n1, "-", n2, "=", n1-n2)
	elif operacion == "*" or operacion == "·"  or operacion == "x"  or operacion == "X":
		print(n1, "*", n2, "=", n1*n2)
	elif operacion == "/":
		print(n1, "/", n2, "=", n1/n2)

	n1 = float(input("Dime un número: "))
	operacion = input("Operación: ")
	n2 = float(input("Dime el otro número: "))

print("Hasta luego")
