# Crea una función "escribir_divisores", 
# que escriba los divisores del número entero
# que se indique como parámetro.

def escribir_divisores(numero: int) -> None:
	for divisor in range(1, numero+1):
		if numero % divisor == 0:
			print(divisor, end=" ")

escribir_divisores(6)
