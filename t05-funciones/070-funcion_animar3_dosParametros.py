# Crea una nueva versión de la función "animar", que escriba 
# "Voy a sacar un 10 en ", seguido del nombre de asignatura 
# que se indique como parámetro. Además, ese texto se debe 
# repetir tantas veces como indique un segundo parámetro.

def animar(nombre, veces):
	for i in range(veces):
		print("Voy a sacar un 10 en "+nombre)

animar("IPE2", 5)
animar("Programación", 6)
