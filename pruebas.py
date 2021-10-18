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
    sumaColumnas = 0
    for e in range(0,5):
        sumaColumnas += tabla[e][i]
    print("suma columna indice", i, " = ", sumaColumnas)


for i in range(0,len(linea)):
    print("suma linea ", i, " = ", sum(tabla[i]))