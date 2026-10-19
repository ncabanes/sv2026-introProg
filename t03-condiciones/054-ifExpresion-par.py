# Pide al usuario un número entero 
# y usa un "if" en formato de expresión 
# para decir si es par o impar.

n = int(input("Dime un número: "))

if n % 2 == 0:
	par = True
else:
	par = False
print(par)

par = True if n % 2 == 0 else False
print(par)

print("Es par" if n % 2 == 0 else "Es impar")
