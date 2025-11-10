secret_number = 777
number_user = int(input("Introduce tu número aquí: "))

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

while secret_number != number_user:
    print("\"¡Ja, ja! ¡Estás atrapado en mi bucle!\"")
    number_user = int(input("Introduce tu número aquí: "))

print("¡Bien hecho, muggle! Eres libre ahora.")