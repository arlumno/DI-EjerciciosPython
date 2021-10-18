# Ejercicio1
# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y
# posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su
# cubo.
'''
import random

laLista = []
for i in range(10) :
    laLista.append(random.randrange(1,10))
print(laLista)
for i in range(0,len(laLista)):
    print(laLista[i], " - ", laLista[i]**2, " - ", laLista[i]**3)
'''


# Ejercicio2
# Realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas
# entre 0 y 10). A continuación, debe mostrar: todas las notas, la nota media, la nota más alta
# que ha sacado y la menor
import random
'''
listaNotas = []

while len(listaNotas) < 5:
    nota = int(input("Indica tu nota"))
    if nota in range(11):
        listaNotas.append(nota)
    else:
        print("la nota debe ser entre 0 y 10")
print("Notas: ",listaNotas)
print("Nota media: ", sum(listaNotas)/len(listaNotas))
print("Nota mas alta: ", max(listaNotas))
print("Nota mas baja: ",min(listaNotas))

# Ejercicio3
# Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa
# que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará
# cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes
# datos:
#  Todos los alumnos mayores de edad.
#  Los alumnos mayores (los que tienen más edad)

listaNombres = []
listaEdades = []
continuar = True
while continuar:
    nombre= input("Indica el nombre")
    if nombre == "*":
        continuar = False
    else:
        edad = int(input("Indica su edad"))
        listaNombres.append(nombre)
        listaEdades.append(edad)

print("Mayores de edad:")
for i in range(len(listaEdades)):
    if listaEdades[i] >= 18:
        print(listaNombres[i])

print("Alumnos Mayores:")
for i in range(len(listaEdades)):
    if listaEdades[i] == max(listaEdades):
        print(listaNombres[i], "tiene ", listaEdades[i], " años")

'''
# Ejercicio4
# Diseñar el algoritmo correspondiente a un programa, que:
#  Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
#  Carga la tabla con valores numéricos enteros.
#  Suma todos los elementos de cada fila y todos los elementos de cada columna
# visualizando los resultados en pantalla.
import random

tabla = []
for i in range(5):
    linea = []
    for e in range(5):
        linea.append(random.randrange(0,10))
    tabla.append(linea)

print("Tabla 5x5 creada: ")
print(tabla)

for i in range(0,5):
    print("suma linea indice ", i, " = ", sum(tabla[i]))

for i in range(0,5):
    sumaColumnas = 0
    for e in range(0,5):
        sumaColumnas += tabla[e][i]
    print("suma columna indice", i, " = ", sumaColumnas)
