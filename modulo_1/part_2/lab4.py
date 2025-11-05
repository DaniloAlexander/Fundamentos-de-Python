nombrePlanta = input("Ingresa el nombre de la planta: ")
plantaFavorita = "Espatifilo"
if nombrePlanta == plantaFavorita:
    print("Si, ¡El Espatifilo! es la mejor planta de todos los tiempos!")
elif nombrePlanta == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print("¡Espatifilo!, ","No ¡",nombrePlanta,"!", sep="")