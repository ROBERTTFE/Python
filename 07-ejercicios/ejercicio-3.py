""" 
Ejercicio 3.
    - Escribir un programa que muestre los cuadrados (un número multiplicado por si mismo) 
    de los 60 primeros números naturales. Resolver con for y con while
"""

# print("\n**************** Ejercicio 3 *****************")

# Con for
for numero in range(1, 61):
    print(f"El cuadrado de {numero} es: {numero * numero}")
    
# Con while
contador = 1
while contador <= 60:
    print(f"El cuadrado de {contador} es: {contador * contador}")
    contador = contador + 1