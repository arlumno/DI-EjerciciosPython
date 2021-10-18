# Ejercicio 1
# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
"""
A = int(input("Indica el primer cateto\n"))
B = int(input("Indica el segundo cateto\n"))
print((A*A+B*B)** (1/2))
"""

# Ejercicio 2
# Un alumno desea saber cual será su calificación final en la materia de
# Matemáticas. Dicha calificación se compone de los siguientes
# porcentajes:
# • 55% del promedio de sus tres calificaciones parciales.
# • 30% de la calificación del examen final.
# • 15% de la calificación de un trabajo final.
"""
parcial1 = int(input("Indica la nota del Primer Parcial\n"))
parcial2 = int(input("Indica la nota del Segundo Parcial\n"))
parcial3 = int(input("Indica la nota del Tercer Parcial\n"))
examenFinal = int(input("Indica la nota del Examen Final\n"))
trabajoFinal = int(input("Indica la nota del Trabajo Final\n"))

notaFinal = ((parcial1 + parcial2 + parcial3)/3)*0.55 + examenFinal*0.3 + trabajoFinal*0.15
print("La nota final es", notaFinal)
"""
# Ejercicio 3
# Dadas dos variables numéricas A y B, que el usuario debe teclear, se
# pide realizar un algoritmo que intercambie los valores de ambas
# variables y muestre cuanto valen al final las dos variables.
"""
A = int(input("Indica el valor de A\n"))
B = int(input("Indica el valor de B\n"))
A,B = B,A
print("Valor de A: ", A)
print("Valor de B: ", B)
"""

# Ejercicio 4
# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS
# segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T
# segundos. Escribir un algoritmo que determine la hora de llegada a la
# ciudad B.
"""
A = "Vigo"
B = "A Coruña"
HH = int(input("Indica la Hora de salida \n"))
MM = int(input("Los Minutos\n"))
SS = int(input("Los Segundos\n"))
print("Salida de", A," a las ", HH, ":", MM,":", SS)
T = int(input("¿Cuanto dura el trayecto desde "+ A + " a " + B + " (en segundos)?\n"))

print("Tiempo de viaje", T, "segundos")

segundosHoraLlegada = HH*3600 + MM*60 + SS + T

HH2 = segundosHoraLlegada // 3600
MM2 = segundosHoraLlegada%3600//60
SS2 = segundosHoraLlegada%60

print("Llegada estimada, a las ", HH2, ":", MM2,":", SS2)
"""

# Ejercicio 5
# Pedir el nombre y los dos apellidos de una persona y mostrar las
# iniciales.
'''
nombre = input("Indica tu nombre\n");
apellido1 = input("Indica tu primer apellido\n");
apellido2 = input("Indica tu segundo apellido\n");
iniciales = nombre[0] + apellido1[0]  + apellido2[0]
print(iniciales.upper())
'''

