#comprobando si esta encendio el panel
panel = 15
mascara = 4
if panel & mascara:
    print("El bit 2 está ENCENDIDO")
else:
    print("El bit 2 está APAGADO")

#encender el bit 2 en el panel1
panel1 = 11
mascara = 4
panel_en1 = panel1 | mascara
print(panel_en1)

#apagar el bit 2 en el panel2
panel2 = 15
mascara = 4
panel_inv1 = panel2 & ~mascara
print(panel_inv1)

#invertir el bit 2 en el panel3

#primer togg
panel3 = 15
mascara = 4
panel_inv2 = panel3 ^ mascara
print(panel_inv2)

#segundo togg
panel4 = 11
mascara = 4
panel_inv3 = panel4 ^ mascara
print(panel_inv3)