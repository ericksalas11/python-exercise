print('¡Hola! ¿Como te llamas?')

miNombre = input("")

print('Bueno, ' + miNombre + ', estoy pensando en un núsmero entre 1 y 20.')

numero = 25
usuario = 0

while usuario != numero:
    usuario = int(input("¿En que numero estoy pensando?"))

    if usuario>numero:
        print("Es un numero menor...")

    elif usuario<numero:
        print("Es un numero mayor!")

    else:
        print("Correcto!, adivinaste el número!!!")
        