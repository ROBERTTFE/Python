"""  
8. ¿Cuánto es el X por ciento de X número?
                ej. 20% de 150
"""

# print("\n**************** Ejercicio 8 *****************")

porcentaje = float(input("Ingrese el porcentaje: "))
numero = float(input("Ingrese el número: "))
resultado = (porcentaje / 100) * numero
print(f"{porcentaje}% de {numero} es: {resultado}")
