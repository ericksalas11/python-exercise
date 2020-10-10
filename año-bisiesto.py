print("¿Quieres saber si un año es bisiesto?")

print("Digite un año:")
anio = int(input())
if (anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 00):
    print("El año es Bisiesto")

else:
        print("El año no es bisiesto")
