# Pide al usuario un número de mes (del 1 al 12) y respóndele 
# si tiene 31 días, 30 días o 28 días (supondremos que se 
# trata de un año no bisiesto).

# Versión 3, con "match"

n = int(input("Dime un numero del mes "))
match n:
	case 1 | 3 | 5 | 7 | 8 | 10 | 12:
		print("Tiene 31 dias")
	case 2:
		print("Tiene 28 dias")
	case 4 | 6 | 9 | 11:
		print("Tiene 30 dias")
	case _:
		print("No es un número de mes válido")
