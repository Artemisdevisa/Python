



def generadorFarmacia():
    i = 1
    while True:
        yield f"F - {i}"
        i += 1

def generadorPerfurmeria():
    i = 1
    while True:
        yield f"P - {i}"
        i += 1


def funcion_padre(funcion):
    gen = funcion()  # Se obtiene el generador llamando a la función generadora
    def fn_hija():
        print("Su turno es: ")
        turno = next(gen)  # Se obtiene el siguiente valor del generador
        print(turno)  # Se imprime el turno
        print("Aguarde \n"
              "y será atendido")
    return fn_hija


def generadorCosmetico():
    i = 1
    while True:
        yield f"C - {i}"
        i += 1

# Aplicar el decorador
generadorCosmeticoDecorado = funcion_padre(generadorCosmetico)

# Llamar a la función decorada varias veces
generadorCosmeticoDecorado()
generadorCosmeticoDecorado()
generadorCosmeticoDecorado()
