def suma():
    n1 = int(input("número 1: "))
    n2 = int(input("número 2: "))
    print(n1 + n2)
    print("Gracias por sumar" + n1+n2)

try:
    suma()
except TypeError:
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Ese no es un número")
else:
    print("Hiciste todo bien")

finally:
    print("Eso fue todo")