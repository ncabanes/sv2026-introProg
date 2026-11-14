# El usuario deberá adivinar un número oculto. Tras cada intento, 
# deberás decirle si se ha pasado o se ha quedado corto.

oculto = 63

intento = int(input("Dime un número: "))
while intento != oculto:
	
	if intento > oculto:
		print("Te has pasado")
	elif intento < oculto:
		print("Te has quedado corto")
		
	intento = int(input("Dime un número: "))

print("Acertaste!")
