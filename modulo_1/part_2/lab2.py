number1 = int(input("Ingresa un número:"))
number2 = int(input("Ingresa un número:"))
number3 = int(input("Ingresa un número:"))

numero_grande = number1

if number2 > numero_grande:
    numero_grande = number2

if number3 > numero_grande:
    numero_grande = number3

print("El número más grande es: ", numero_grande)