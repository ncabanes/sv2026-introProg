# 11. Ampliando la idea anterior, crea una 
# función "escribir_al_reves(texto)", que 
# escriba al revés el texto que se indique 
# como parámetro. Incluye un programa de 
# prueba, que escriba al revés el texto que 
# elija el usuario.

def escribir_al_reves(texto: str) -> None:
	longitud = len(texto)
	for i in range(longitud-1, -1, -1):
		print(texto[i], end="")
	
nombre = input("Dime tu nombre ")
escribir_al_reves(nombre)

