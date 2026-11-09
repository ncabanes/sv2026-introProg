# Calculadora

# Crea un programa que te pida un número, un operador y otro 
# número, y muestre el resultado de esa operación, así:
# 
# Dime un número: 3
# Operación? +
# Dime el otro número: 5
# 3 + 5 = 8

a = float(input("Dime un número: "))
operacion = input("Operación? ")
b = float(input("Dime el otro número: "))

if operacion == "+":
	print(a , "+", b, "=", a+b)
elif operacion == "-":
	print(a , "-", b, "=", a-b)
elif operacion == "*" or operacion == "·" or operacion == "x" or operacion == "X":
	print(a , "*", b, "=", a*b)
elif operacion == "/":
	print(a , "/", b, "=", a/b)
elif operacion == "**" or operacion == "^":
	print(a , "**", b, "=", a**b)
