# Crea una funcion "elevar(n1, n2)", de modo que
# print(elevar(3.5, 2))
# se comporte igual que
# print(3.5 ** 2)

def elevar(n1: float, n2: float) -> float:
	return n1 ** n2

print(3.5 ** 2)
print(elevar(3.5, 2))
