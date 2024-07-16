import re

def verificar_cp(cp):
    resultado = re.search(r'\w{2}\d{4}', cp)
    if resultado:
        return resultado.group()
    else:
        return "El código postal ingresado no es correcto"

print(verificar_cp('MMMXX1234'))