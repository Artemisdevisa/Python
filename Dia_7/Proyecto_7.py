class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"El cliente: {self.nombre} {self.apellido} con nro° {self.numero_cuenta} y su balance: {self.balance}"

    def retirar(self, cantidad):
        if cantidad > self.balance:
            return "Error: Fondos insuficientes"
        else:
            self.balance -= cantidad
            return f"Retiraste {cantidad} soles"

    def depositar(self, cantidad):
        self.balance += cantidad
        return f"Depositaste {cantidad} soles"


def crear_cliente():
    objCliente = Cliente('Joseph', 'Vidaurre', '72807123', 1600)  # Balance como número
    return objCliente


def inicio():
    obj = crear_cliente()
    opc = False
    while not opc:
        print(obj)  # Imprimir estado actual del cliente
        valor = int(input("Seleccione una opción: \n Retirar (1) - Depositar (2) - Salir (3)\n-> "))
        if valor == 1:
            cantidad = int(input("Ingrese la cantidad a retirar: "))
            print(obj.retirar(cantidad))
        elif valor == 2:
            cantidad = int(input("Ingrese la cantidad a depositar: "))
            print(obj.depositar(cantidad))
        elif valor == 3:
            opc = True
        else:
            print("Opción no válida")


inicio()
