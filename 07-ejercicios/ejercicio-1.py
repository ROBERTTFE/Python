""" 
Ejercicio 1.
    - Crear 3 variables una "pais", otra "continente" y la otra "año (year)"
    - Mostrar su valor por pantalla
    - Poner un comentario diciendo el tipo de dato
"""

# print("\n**************** Ejercicio 1 *****************")

pais = "España" # String
pais = input("Dime un pais: ")

if pais == "España":
    print("El pais es España")
else:
    print("El pais no es España")

continente = "Europa" # String
continente = input("Dime un continente: ")

if continente == "Europa":
    print("El continente es Europa")
else:
    print("El continente no es Europa")
    
year = 2026 # Integer
year = int(input("¿En qué año Estamos? "))

if year >= 2026:
    print("Estamos despues del 2026")
else:
    print("Es un año antes del 2026")