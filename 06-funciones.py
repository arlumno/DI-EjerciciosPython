# EJERCICIO 1
# Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es
# múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el
# primero es múltiplo del segundo.


def EsMultiplo(num1, num2):
    resultado = False
    if num2 % num1 == 0:
        resultado = True
    return resultado


num1 = int(input("Dime un numero entero"))
num2 = int(input("Dime otro numero entero"))

if EsMultiplo(num1, num2):
    print(num1, " es multiplo de ", num2)
else:
    print(num1, " NO es multiplo de ", num2)


# EJERCICIO 2
# Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el
# valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el
# máximo y el mínimo, utilizando la función anterior.
def calcularMaxMin(numeros):
    print("El número máximo es: ", max(numeros))
    print("El número mínimo es: ", min(numeros))


listaNumeros = []

while True:
    numeroNuevo = int(input("Dime un numero, o pon 0 para terminar"))
    if numeroNuevo == 0: break
    listaNumeros.append(numeroNuevo)
    calcularMaxMin(listaNumeros)


# EJERCICIO 3
# El día juliano correspondiente a una fecha es un número entero que indica los días que han
# transcurrido desde el 1 de enero del año indicado. Queremos crear un programa principal que
# al introducir una fecha nos diga el día juliano que corresponde. Para ello podemos hacer las
# siguientes subrutinas:
#  LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
#  DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
#  EsBisiesto: Recibe un año y nos dice si es bisiesto.
#  Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano


def Calcular_Dia_Juliano():
    fecha = LeerFecha()
    # esto es para que sea mas legible
    dia = fecha[0]
    mes = fecha[1]
    anio = fecha[2]
    dias = 0
    for i in range(1,mes):
        dias += DiasDelMes(i, anio)
    dias += dia
    print("El día juliano es: ", dias)

def LeerFecha():
    print("Indica un fecha:")
    fecha = []
    fecha.append(int(input("El día:")))
    fecha.append(int(input("El mes:")))
    fecha.append(int(input("El año:")))
    if comprobarfecha(fecha) == False:
        print("Fecha No Valida")
        exit()
    return fecha

def DiasDelMes(mes,anio):
    mes31dias = [1, 3, 5, 7, 8, 10, 12]
    if mes in mes31dias:
        dias = 31
    elif mes == 2:
        # bisiesto
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            dias = 29
        else:
            dias = 28
    else:
        dias = 30
    return dias

def comprobarfecha(fecha):
    dia = fecha[0]
    mes = fecha[1]
    anio = fecha[2]
    error = True
    diaMax = 30
    mes31dias = [1, 3, 5, 7, 8, 10, 12]

    if mes <= 12 and mes > 0:
        if mes in mes31dias:
            diaMax = 31
        elif mes == 2:
            # bisiesto
            if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
                diaMax = 29
            else:
                diaMax = 28
        if dia <= diaMax and dia > 0:
            error = False
    if error:
        return False
    else:
        return True

Calcular_Dia_Juliano()
