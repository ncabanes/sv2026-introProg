# Crea una función "es_primo", que devuelva 
# True si el número que se le pasa como 
# parámetro es primo, o False en caso 
# contrario.

def es_primo(numero: int) -> bool :
	cantidad = 0
	for divisor in range(1, numero+1):
		if numero % divisor == 0:
			cantidad += 1
	if cantidad == 2:
		return True
	else:
		return False


if es_primo(13):
	print("Empezamos bien")
else:
	print("Mal")

