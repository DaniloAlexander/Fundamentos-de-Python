bloques = int(input("Ingresa el número de bloques: "))
nivel = 1

for altura in range(bloques):
    if bloques < nivel:
        break
    bloques = bloques - nivel
    nivel += 1
print("La altura de la pirámide:", altura)


#bloques = int(input("Ingresa el número de bloques: "))
#nivel = 1
#altura = 0

#while bloques >= nivel:
#    bloques = bloques - nivel
#    nivel += 1
#    altura += 1

#print("La altura de la pirámide:", altura)
