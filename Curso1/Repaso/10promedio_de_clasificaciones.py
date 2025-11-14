notas = []
total = 0
for i in range(5):
    i = int(input("Ingrese la nota: "))
    notas.append(i)
    total += i
print(total / len(notas))