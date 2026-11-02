# Crea una función "suma_hasta", que devuelva la suma de 
# los números desde 1 hasta el que se indique como parámetro:

# print(suma_hasta(10))

def suma_hasta(n):
	suma = 0
	for i in range(1, n+1):
		suma += i
	return suma

print(suma_hasta(10))

