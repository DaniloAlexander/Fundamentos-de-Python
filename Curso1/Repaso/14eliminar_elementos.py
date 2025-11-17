colores = ["Azul","Negro","Blanco","Gris"]
print("Lista de Colores: ",colores)
eliminar = input("Que color desea eliminar: ")

if eliminar in colores:
    indice = colores.index(eliminar)
    del colores[indice]
    print("Color eliminado correctamente")
else:
    print("Ese color no esta")

print(colores)
print(len(colores))