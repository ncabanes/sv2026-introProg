# Crea una función "mayor_de_3", que reciba tres números 
# como parámetros y devuelva el valor del mayor 
# de los tres:
# 
# print(mayor_de_3(5,6,7))
# 
# 7

def mayor_de_3(n1: float, n2: float,
		n3: float) -> float:
			
	if n1 >= n2 and n1 >= n3:
		return n1
	elif n2 >= n1 and n2 >= n3:
		return n2
	else:
		return n3
	
print( mayor_de_3(5, 6, 7) )
print( mayor_de_3(7, 6, 5) )
print( mayor_de_3(7, 7, 5) )
print( mayor_de_3(7, 5, 5) )
print( mayor_de_3(5, 5, 5) )

mayor_10_20_30 = mayor_de_3(10, 20, 30)
print(mayor_10_20_30)
	


