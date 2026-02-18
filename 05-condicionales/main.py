""" 
Condicional IF

si se cumple una condicion
   hacer esto
si no se cumple
   hacer esto otro

# Operadores de comparación
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores lógicos
and -> Y
or  -> O
!   -> negación
not -> NO

"""

# print("\n**************** Ejemplo 1 *****************")
# color = input("Adivina mi color favorito: ")

# if color == "rojo":
#     print("El color es Rojo")
# else:
#     print("El color no es mi favorito")


# print("\n**************** Ejemplo 2 *****************")
# # year = 2026
# year = int(input("¿En qué año Estamos? "))

# if year >= 2026:
#    print("Estamos del 2026 en adelante")
# else:
#    print("Es un año anterior al 2026")

# print("\n**************** Ejemplo 3 *****************")

# nombre = "Rafael"
# ciudad = "Los Realejos"
# pais = "España"
# edad = 40
# mayoria_edad = 18

# if edad >= mayoria_edad:
#    print(f"{nombre} es mayor de edad!!!")

#    if pais != "España":
#       print("El usuario no está en España")
#    else:
#       print(f"El usuario esta en España y en {ciudad}")

# else:
#    print(f"{nombre} no es mayor de edad")

# print("\n**************** Ejemplo 4 *****************")

# dia = int(input("Introduce el número del dia de la semana: "))

# if dia == 1:
#    print("Es lunes")
# else:
#    if dia == 2:
#       print("Es martes")
#    else:
#       if dia == 3:
#          print("Es miércoles")
#       else:
#          if dia == 4:
#             print("Es jueves")
#          else:
#             if dia == 5:
#                print("Es viernes")
#             else:
#                print("Es fin de semana")


# # -------
# if dia == 1:
#    print("Es lunes")
# elif dia == 2:
#    print("Es martes")
# elif dia == 3:
#    print("Es miércoles")
# elif dia == 4:
#    print("Es jueves")
# elif dia == 5:
#    print("Es viernes")
# else:
#    print("Es fin de semana")


#Ejemplo 5
# print("\n**************** Ejemplo 5 +++++++++++++++++++")

# edad_minima = 18
# edad_maxima = 65
# valor = input("Tienes edad para trabajar? Ingresa tu edad: ")
# edad_oficial = int(valor)
# print(type(edad_oficial))

# if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
#    print("Estas en edad de trabajar")
# else:
#    print("No estas en edad de trabajar")
   
   
print("\n**************** Ejemplo 6 ------------------")
pais = input("Dime un pais de habla hispana: ")

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana!!!")
else:
    print(f"{pais} no es un pais de habla hispana :( ")
#################################################################
if pais == "Mexico" and pais == "España" and pais == "Colombia":
    print(f"{pais} No es un pais de habla hispana!!!")
else:
    print(f"{pais} Si es un pais de habla hispana :( ")
