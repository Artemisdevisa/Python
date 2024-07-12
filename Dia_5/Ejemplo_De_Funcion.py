precios_cafe = [('capuchino', 1.5), ('Expresso', 2.5), ('Moka', 1.9)]

def cafe_mas_caro(lista_precios):
    precio = 0
    cafe = ''
    for val1, val2 in lista_precios:
        if precio < val2:
            precio = val2
            cafe = val1
        else: pass


    return(precio, cafe)

print(cafe_mas_caro(precios_cafe))