# Función escribir_pares_entre(n1, n2)

def escribir_pares_entre(n1:int, n2:int) -> None:
	for i in range(n1, n2+1):
		if i % 2 == 0:
			print (i, end= " ")

escribir_pares_entre(11,20)
# 12 14 16 18 20
