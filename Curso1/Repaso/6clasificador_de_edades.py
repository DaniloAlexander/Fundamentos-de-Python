edad = int(input("Ingrese su edad: "))

if edad < 13:
    print("Niño")
elif edad <= 17:
    print("Adolescente")
elif edad <= 64:
    print("Adulto")
else:
    print("Adulto Mayor")