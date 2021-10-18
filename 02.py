## Estructuras alternativas

# Ejercicio 1
# • Algoritmo que pida un número y diga si es positivo, negativo o 0.
'''

numero = int(input("Indica un número\n"))
if numero > 0:
    print('es Positivo')
elif numero < 0:
    print('es negativo')
else:
    print ('es neutro')
'''

# Ejercicio 2
# • Escribe un programa que pida un nombre de usuario y una
# contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has
# entrado al sistema”, sino se da un error.
'''
usuario = input('Indica tu usuario\n')
clave = input('Indica tu contraseña\n')
if usuario == 'pepe' and clave == 'asdasd':
    print ('Has entrado al sistema')
else:
    print ('***Crecenciales erroneas***')
'''

# Ejercicio 3
# • Algoritmo que pida tres números y los muestre ordenados (de mayor
# a menor)
'''
numero1 = int(input("Indica un número\n"))
numero2 = int(input("Indica otro número\n"))
numero3 = int(input("Indica un último número\n"))

if numero1 > numero2:
    if numero1 > numero3:
        n3 = numero1
        if numero2 > numero3:
            n1, n2 = numero3, numero2
        else:
            n1, n2 = numero2, numero3
    else:
        n1, n2, n3 = numero2, numero1, numero3
else:
    n1 = numero1
    if numero2 > numero3:
        n2, n3 = numero3, numero2
    else:
        n2, n3 = numero2, numero3
print(n3, ", ",n2, ", ",n1)
'''

# Ejercicio 4
# • Escribe un programa que pida una fecha (día, mes y año) y diga si es
# correcta.

'''
dia = int(input("Indica un día\n"))
mes = int(input("Indica un mes\n"))
anio = int(input("Indica un año\n"))
error = True
diaMax = 30
mes31dias = [1,3,5,7,8,10,12]

if mes <= 12 and mes > 0:
    if mes in mes31dias:
        diaMax = 31
    elif mes == 2:
        #bisiesto
        if anio%4 == 0 and (anio%100 != 0 or anio%400 == 0):
            diaMax = 29
        else:
            diaMax = 28

    if dia <= diaMax and dia >0:
        error = False

if error:
    print ('Fecha NO Válida')
else:
    print('Fecha Válida')
'''

## Estructuras repetitivas

# Ejercicio 1
# • Crea una aplicación que pida un número y calcule su factorial (El
# factorial de un número es el producto de todos los enteros entre 1 y
# el propio número y se representa por el número seguido de un signo
# de exclamación. Por ejemplo 5! = 1x2x3x4x5=120)
'''
numero = int(input("Indica un número\n"))
resultado = 1
for i in range(2,numero+1):
    resultado *= i

print('El factorial de',numero, " es:", resultado)
'''

# Ejercicio 2
# • Algoritmo que pida números hasta que se introduzca un cero. Debe
# imprimir la suma y la media de todos los números introducidos.

'''
numero = 1
while numero != 0:
    numero = int(input("Indica un número\n"))
print('Fin del programa')
'''

# Ejercicio 3
# • Realizar una algoritmo que muestre la tabla de multiplicar de un
# número introducido por teclado.
'''
print('Tabla del', numero, ":\n")
for i in range(1, numero + 1):
    print(numero, "x", i, " = ", i * numero)

'''
# Ejercicio 4
# • Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4
# y 5.
'''
for i in range(1,6):
    print('\nTabla del', i, ":")
    for e in range(1, i + 1):
        print(i, "x", e, " = ", e * i)
'''

# Ejercicio 5
# • Escribe un programa que diga si un número introducido por teclado
# es o no primo. Un número primo es aquel que sólo es divisible entre
# él mismo y la unidad. Nota: Es suficiente probar hasta la raíz cuadrada
# del número para ver si es divisible por algún otro número.

numero = int(input("Indica un número\n"))
primo = True

for i in range(2, int(numero** 0.5)+1):
    if numero%i == 0:
        primo = False
        break
if primo:
    print("ES primo")
else:
    print("NO es primo")
