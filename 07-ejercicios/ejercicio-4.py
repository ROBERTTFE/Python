""" 
Ejercicio 4. 
    - Pedir dos números al usuario y hacer todas las operaciones básicas de una calculadora y mostrarlo por pantalla
"""
n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))

print("Operaciones matemáticas básicas + - * /")
print(f"La suma de {n1} + {n2} = {n1 + n2}")
print(f"La resta de {n1} - {n2} = {n1 - n2}")
print(f"La multiplicación de {n1} * {n2} = {n1 * n2}")
print(f"La división de {n1} / {n2} = {n1 / n2}")

# print("\n**************** Ejercicio 4 *****************")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "No se puede dividir por cero"

print(f"\nResultados:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
