""" 
Ejercicio 3.
    - Escribir un programa que muestre los cuadrados (un número multiplicado por si mismo) 
    de los 60 primeros números naturales. Resolverlo con for y con while
"""

for num in range(1,61):
    print(f"{num} el cuadrado es: {num * num}")

print("*********Usando While***********")
num1 = 0
while num1 < 61:
    print(f"{num1} el cuadrado es: {num1**2}")
    num1 += 1
    

# print("\n**************** Ejercicio 3 *****************")

print("**************** Con FOR *****************")

for numero in range(1, 61):
    print(f"El cuadrado de {numero} es: {numero * numero}")
    
print("**************** Con WHILE *****************")
    
contador = 1
while contador <= 60:
    print(f"El cuadrado de {contador} es: {contador * contador}")
    contador = contador + 1