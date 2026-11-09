# Crea un programa que escriba el calendario de un mes,
# tras preguntarte cuántos días tiene un mes y qué día
# de la semana empieza:
# 
# Días del mes: 31
# Comienza en (1=lunes, 7=domingo): 4
# 
#  L  M  X  J  V  S  D
#          01 02 03 04 
# 05 06 07 08 09 10 11 
# 12 13 14 15 16 17 18 
# 19 20 21 22 23 24 25 
# 26 27 28 29 30 31 

dias = int(input("Días del mes: "))
comienzo = int(input("Comienza en (1=lunes, 7=domingo): "))

print(" L  M  X  J  V  S  D")
print("   " * (comienzo-1), end="")
dias_escritos = comienzo-1

#Escribimos todos los días
for i in range(1, dias+1):
    
    # Si es menor de 10, debe empezar por 0 (o espacio)
    if i < 10:
        print("0", end="")
    
    # Mostramos el número y lo contamos
    print(i, end=" ")
    dias_escritos += 1
    
    # Y saltamos de línea si ya llevamos 7
    if dias_escritos == 7:
        dias_escritos = 0
        print()
