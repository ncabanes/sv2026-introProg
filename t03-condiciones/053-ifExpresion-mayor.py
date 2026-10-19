# Usa un "if" en formato de expresión para
# mostrar el mayor de dos números enteros

n1 = int(input("Dime un número: "))
n2 = int(input("Dime otro: "))

if n1 > n2:
	mayor = n1
else:
	mayor = n2
print(mayor)

mayor = n1 if n1 > n2 else n2
print(mayor)

print(n1 if n1 > n2 else n2)
