# Pide al usuario un número de mes (del 1 al 12) y respóndele 
# si tiene 31 días, 30 días o 28 días (supondremos que se 
# trata de un año no bisiesto).

# Versión 2, compacta, con "or"

n = int(input("dime un numero del mes")
if n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
	print("Tiene 31 dias")
elif n==2:
	print("Tiene 28 dias")
elif n==4 or n==6 or n==9 or n==11:
	print("Tiene 30 dias")
else:
	print("te has equivocado")
