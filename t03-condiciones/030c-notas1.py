# 0 a 4 - Suspenso
# 5, 6 - Aprobado
# 7, 8 - Notable
# 9, 10 - Sobresaliente

num=int(input("Dime tu nota "))
if num<5:
	print("suspenso")
elif num<7:
	print("aprobado")
elif num<9:
	print("notable")
elif num<11:
	print("sobresaliente")
else:
	print("error")
