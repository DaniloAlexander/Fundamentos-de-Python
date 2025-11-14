listaSuper = ["Leche", "Pan","Azúcar","Mostaza","Cereal"]

for i in range(len(listaSuper)):
    print(i + 1,".", listaSuper[i], sep="")

valorsec = int(input("Ingrese un número: "))
print("El producto que selecionaste es: ", listaSuper[valorsec - 1])