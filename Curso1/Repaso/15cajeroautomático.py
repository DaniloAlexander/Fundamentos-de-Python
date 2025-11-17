#variables de inicio de sesión
contrasenha = "123"
intentos = 1
#funciones del cajero
saldoinicial = 1000
menu = ["Consultar Saldo","Depositar dinero","Retirar dinero","Salir"]
#pedir contraseña por primera vez
intentoAcceso = input("Ingrese contraseña: ")
#el usuario erro la contraseña
while intentoAcceso != contrasenha:
    if intentos == 3:
        print("ACCESO DENEGADO")
        break
    intentoAcceso = input("Contraseña incorrecta, Ingrese la contraseña: ")
    intentos += 1
#el usuario acerto la contraseña
if contrasenha == intentoAcceso:
#for solo para mostrar el menu
    for i in range(len(menu)):
        print(i + 1,menu[i])
#adentro del cajero
    accion = int(input("Seleccione la transacción que desae realizar: "))
#el usuario seleciono consultar el saldo
    if accion == indice:
        print("Tu saldo es: ",saldoinicial)
#el usuario seleciono depositar dinero
#el usuario seleciono retirar dinero
#el usuario seleciono salir