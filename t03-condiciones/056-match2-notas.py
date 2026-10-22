# 0 a 4 - Suspenso
# 5, 6 - Aprobado
# 7, 8 - Notable
# 9, 10 - Sobresaliente

nota=int(input("Dime tu nota "))

match nota:
	case 1 | 2 | 3 | 4:
		print("suspenso")
	case 5 | 6:
		print("aprobado")
	case 7 | 8:
		print("notable")
	case 9 | 10:
		print("sobresaliente")
	case _:
		print("error")
