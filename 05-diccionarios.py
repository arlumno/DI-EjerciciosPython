# Ejercicio 1
# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de
# apariciones de cada carácter en la cadena.
cadena = input("Escribe una frase")
dicCaracteres = {}
for i in range(len(cadena)):
    if cadena[i] in dicCaracteres:
        dicCaracteres[cadena[i]] += 1
    else:
        dicCaracteres[cadena[i]] = 1
print(dicCaracteres)






# Ejercicio 2
# Vamos a declarar un diccionario para guardar los precios de las distintas frutas. El programa
# pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la
# fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error.
# Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

almacen = {"manzana":0.50,
           "piña":1.50,
           "fresa":2.35,
           "kiwi": 3.59,
           "melocoton":1.20}

continuar= True

while continuar:
    fruta = input("Indica la fruta")
    if fruta in almacen:
        unidades = int(input("Indica las unidades"))
        total = almacen[fruta] * unidades
        print("--- ", unidades,"x",fruta," =", total, "€")
    else:
        print("No tenemos ", fruta, " en el almacen")

    if input("¿Desea hacer otra consulta? escribe 's' para continuar ").lower() != "s":
            continuar = False

