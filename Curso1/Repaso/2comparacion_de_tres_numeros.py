numeroUsuario1 = int(input("Ingrese el primer número: "))
numeroUsuario2 = int(input("Ingrese el segundo número: "))
numeroUsuario3 = int(input("Ingrese el tercer número: "))

if numeroUsuario1 > numeroUsuario2 and numeroUsuario1 > numeroUsuario3:
    print("El primer número es mayor.")
elif numeroUsuario2 > numeroUsuario1  and numeroUsuario2 > numeroUsuario3:
    print("El segundo número es mayor.")
else:
    print("El tercer número es mayor.")
