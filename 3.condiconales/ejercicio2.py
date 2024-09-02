distancia = float(input("Ingrese la distancia en kilometros: "))

if distancia <= 1:
    tarifa = 5
elif distancia <=5:
    tarifa = 5 + (distancia - 1) * 2
else:
    tarifa = 13 + (distancia - 5) * 1.5
print(f"La tarifa del taxi es {tarifa}")

