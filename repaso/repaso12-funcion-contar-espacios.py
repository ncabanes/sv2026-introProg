# 12. Crea una función "cantidad_de_espacios(texto)",
# que reciba un texto y devuelva la cantidad de espacios
# en blanco que contenga. Por ejemplo, para la frase 
# "Hola qué tal", debería devolver 2. Utilízala en 
# un programa de prueba.

def cantidad_de_espacios(texto: str) -> int:
	cantidad = 0
	for i in range(len(texto)):
		if texto[i] == " ":
			cantidad += 1
	
	return cantidad


frase = input("Dime una frase ")
espacios = cantidad_de_espacios(frase)
print("Tiene",espacios,"espacios")
