'''Vamos a crear una app que permita ingresar una nota y evaluar
si es aprobado(5 a 7), notable(8 a 9), sobresaliente(10) y todo
lo que sea menor a esto reprobado'''

nota = int(input("Ingrese su nota: "))

if (nota >= 5 and nota <= 7):
    print("Aprobado")
elif (nota >= 8 and nota <= 8):
    print("Notable")
elif nota == 10:
    print("Sobresaliente")
else:
    print("Reprobo")

