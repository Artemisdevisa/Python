


from random import choice

vidas = 6
palabras = ['pelota', 'lavadora', 'televisor']
palabra = choice(palabras)
npala = ['-' for v in palabra]
print(palabra)
print(list(enumerate(palabra)))


def ingreso():
    return input("Ingrese una letra: ")


def validacion(letra):
    global vidas
    if letra not in palabra:
        vidas -= 1
        print(f"Letra incorrecta. Te quedan {vidas} vidas.")
    else:
        for idx, val in enumerate(palabra):
            if val == letra:
                npala[idx] = letra
        print(f"Acertaste. La palabra queda como {''.join(npala)}")


while vidas > 0 and '-' in npala:
    letra = ingreso()
    validacion(letra)

if vidas == 0:
    print(f"Perdiste. La palabra era: {palabra}")
else:
    print(f"Ganaste. La palabra es: {palabra}")
