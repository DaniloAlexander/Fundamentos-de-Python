vocals = ["a","e","i","o","u","A","E","I","O","U"]
palabra = input("Ingrese una palabra: ")
contador = 0

for i in palabra:
    if i in vocals:
        contador += 1
print("Tu palabra tiene",contador,"vocal" if contador == 1 else "vocales")