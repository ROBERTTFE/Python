"""  
Ejercicio 5.
    - Hacer un programa que muestre todos los números entre dos números que diga el usuario
"""

# print("\n**************** Ejercicio 5 *****************")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print(f"\nNúmeros entre {num1} y {num2}:")
if num1 < num2:
    for i in range(num1 + 1, num2):
        print(i)
elif num1 > num2:
    for i in range(num2 + 1, num1):
        print(i)
else:
    print("Los números son iguales, no hay números entre ellos.")
    