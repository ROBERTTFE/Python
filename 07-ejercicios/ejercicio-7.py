"""  
7. Hacer un programa que muestre todo los números impares entre dos números
que ingrese el usuario por teclado.
"""

# print("\n**************** Ejercicio 7 *****************")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print(f"Números impares entre {num1} y {num2}:")
for i in range(num1 + 1, num2 + 1):
    if i % 2 != 0:
        print(i)
        