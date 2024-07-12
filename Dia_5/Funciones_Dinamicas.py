def cantidad_pares(lista_numeros):
    contador = 0
    for val in lista_numeros:
        if val % 2 == 0:
            contador += 1

    return contador

print(cantidad_pares([2, 4, 6]))