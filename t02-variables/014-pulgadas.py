# Conversor de centímetros a pulgadas (ejemplo de "str")

# Pregunta al usuario una cantidad de
# centímetros. Respóndele a cuantas
# pulgadas equivale, usando una frase
# como "xxx centímetros son yyy pulgadas".

cm = float(input("Cuantos centímetros quieres convertir? " ))
pulgadas = cm / 2.54
print( str(cm) + " son " + str(pulgadas) + " pulgadas.")

# print( cm, "son", pulgadas, "pulgadas.")
