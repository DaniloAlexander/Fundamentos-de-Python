palabra = "chupacabra"
usuario = input("Ingrese una palabra: ")
while palabra != usuario:
    if palabra == usuario:
        break
    else:
        print("¡Jajajaja, estas atrapado!")
        usuario = input("Ingrese una palabra: ")

print("Has dejado el bucle con éxito")