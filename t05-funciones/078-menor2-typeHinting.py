# Crea una función "menor", que devuelva el menor de los 
# dos números que se indiquen como parámetro
# 
# n = menor(5,2)
# 
# Nota: esta versión debe emplear "type hinting" (anotación de tipos)

def menor(n1 : float, n2 : float) -> float:
	if n1 < n2:
		return n1
	else:
		return n2


x = menor(7, 5)
print(x)

print(menor(5,7))
print(menor(5,5))
