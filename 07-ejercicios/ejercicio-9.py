"""  
9. Hacer un programa que pida números al usuario indefinidamente hasta que
introduzca 111
"""

# print("\n**************** Ejercicio 9 *****************")

while True:
    numero = int(input("Ingrese un número (111 para salir): "))
    if numero == 111:
        print("¡Hasta luego!")
        break
    