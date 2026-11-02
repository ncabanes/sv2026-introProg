# Crea una función "es_par", que devuelva True o False según si 
# el número entero que se le indica como parámetro es par o no lo es:
# 
# if es_par(20):
#     print("20 es par")

def es_par(numero : int) -> bool:
	if numero % 2 == 0:
		return True
	else:
		return False

n = int(input("Dime un número entero: "))
if es_par(n):
	print("Es par")
else:
	print("Es impar")
