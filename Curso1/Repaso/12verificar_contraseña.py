contrasenha = "Python123"
usuario = input("Ingrese una contraseña: ")
intentos = 2
##El usuario no ingreso la contraseña correcta
while contrasenha != usuario:
## limitador de intentos
    if intentos == 0:
        print("LLEGASTE AL LIMITE")
        break
    usuario = input("ACESSO DENEGADO, INGRESE CONTRASEÑA NUEVAMENTE: ")
    intentos -= 1
##El usuario ingreso la contraseña correcta
if contrasenha == usuario:
    print("ACCESO CONFIRMADO")
