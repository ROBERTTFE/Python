"""
10. Escribe un programa que pida la nota de 8 alumnos y sacar por pantalla 
cuantos han aprobado y cuantos han suspendido.
"""

# print("\n**************** Ejercicio 10 *****************")

aprobados = 0
suspendidos = 0
for i in range(8):
    nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1
print(f"Cantidad de alumnos aprobados: {aprobados}")
print(f"Cantidad de alumnos suspendidos: {suspendidos}")

# print("\n**************** Ejercicio 10 *****************")


