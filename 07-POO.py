# Ejercicio 1
# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye
# los siguientes métodos para la clase:
# • Un constructor, donde los datos pueden estar vacíos.
# • Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
# datos.
# • mostrar(): Muestra los datos de la persona.
# • esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.


class Persona:
    def __init__(self,nombre = "", edad = 0, dni = ""):
            self.nombre = nombre
            self.edad = edad
            self.dni = dni

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def dni(self):
        return self._dni

    @nombre.setter
    def nombre(self,nombre):
        if len(nombre) > 1 :
            self._nombre = nombre
        else:
            print("Nombre no válido")

    @edad.setter
    def edad(self, edad):
        if edad > 0 and edad < 125:
            self._edad = edad
        else:
            print("Edad no válida")

    @dni.setter
    def dni(self, dni):
        if len(dni) == 9:
            self._dni = dni
        else:
            print("Dni no válido")


    def mostrar(self):
        print("Nombre:", self.nombre, "Dni:", self.dni ,"Edad:",self.edad, "años" )

    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False
ejemplo = Persona("Armando",33,"55446699U")
#ejemplo.mostrar()
#ejemplo.esMayorDeEdad()


# Ejercicio 2
# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona)
# y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional.
# Construye los siguientes métodos para la clase:
# • Un constructor, donde los datos pueden estar vacíos.
# • Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, solo ingresando o retirando dinero.
# • mostrar(): Muestra los datos de la cuenta.
# • ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
# negativa, no se hará nada.
# • retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
# rojos.

class Cuenta:
    def __init__(self,titular,cantidad = 0.00):
        self.titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        return self._titular

    @property
    def cantidad(self):
        return self._cantidad

    @titular.setter
    def titular(self,nombre):
        self._titular = nombre

    def mostrar(self):
        print("Datos del Titular:")
        self.titular.mostrar()
        print("Saldo: \n", self.cantidad, "Euros")

    def ingresar(self,importe):
        if importe >= 0:
            self._cantidad += importe
        else:
            print("Error en la operación. Importe negativo")

    def retirar(self,importe):
        self._cantidad -= importe
        if(self._cantidad < 0):
            print("AVISO: su cuenta está en rojos, Saldo actual: ", self.cantidad)

cuenta = Cuenta(ejemplo,300);
cuenta.mostrar()
cuenta.ingresar(3.3)
cuenta.mostrar()
cuenta.retirar(400.09)
cuenta.mostrar()


# Ejercicio 3
# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuentaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la
# cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.
# Construye los siguientes métodos para la clase:
# • Un constructor.
# • Los setters y getters para el nuevo atributo.
# • En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por
# lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular
# es mayor de edad pero menor de 25 años y falso en caso contrario.
# • Además la retirada de dinero sólo se podrá hacer si el titular es válido.
# • El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de
# la cuenta.
# Piensa los métodos heredados de la clase madre que hay que reescribir.