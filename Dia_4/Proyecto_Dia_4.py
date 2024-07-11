from random import *

nombre = input("Ingrese su nombre: ")
numero = randint(1, 100)
print(f"Hola {nombre} e pensado un número entre el 1 y 100 y es: {numero} \n"
      f"Debes adivinarlo, solo tienes 8 intentos")
bool = 8
intento = 0

while bool > 0:
      bool -= 1
      intento = int(input("Ingresa tu intento: "))
      if intento > 100 or intento < 1:
            print("El número no es permitido")
      elif intento < numero:
            print("El número ingresado en menor")
      elif intento > numero:
            print("El número ingresado en mayor")
      else:
            print("El número ingresado es el correcto \n"
                  f"Acertaste en el intento {8 - bool + 1}")
