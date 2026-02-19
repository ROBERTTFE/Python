"""  
6. Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el título de la tabla y luego la multiplicación del 1 al 10.
"""

# print("\n**************** Ejercicio 6 *****************")

for i in range(1, 11):
    input("Pulsa enter para continuar...")
    print(f"\nTabla del {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
        