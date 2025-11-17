valor1 = int(input("Ingresa un número: "))
valor2 = int(input("Ingresa un número: "))
tipoDeOperacion = input("Que tiṕo de opereación deseas realizar? ")

if tipoDeOperacion == "suma":
    print(valor1 + valor2)

elif tipoDeOperacion == "resta":
    print(valor1 - valor2)

elif tipoDeOperacion == "multiplicacion":
    print(valor1 * valor2)

elif tipoDeOperacion == "division":
    if valor2 == 0:
        print("error matemático")
    else:
        print(valor1 / valor2)

else:
    print("Operación inválida")