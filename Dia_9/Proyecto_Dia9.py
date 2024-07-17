import os
import re
import datetime

grande = ""
cadenita = []
ruta = "C:\\Users\\jenny\\Desktop\\Mi_Gran_Directorio"
'''------------------------------------------------------------------------------------------'''

def lectura(ruta):
    for carpeta, subcarpeta, archivos in os.walk(ruta):
        for arch in archivos:
            abrir = open(carpeta + "\\" + arch, 'r')
            salida = abrir.read()
            resultado = re.search(r'N\w{3}-\d{5}', salida)
            if resultado:
                cadenita.append(arch+"-"+resultado.group())

lectura(ruta)

def formato():
    grande = f'Fecha de búsqueda:\t\t\t\t[{datetime.date.today()}]\n'
    grande += ("ARCHIVO\t\t\t\tNRO.SERIE\n"
              "-------\t\t\t\t----------\n")
    for val in cadenita:
        grande += f"{val.split("-")[0]}\t\t\t\t{val.split("-")[1]}\n"
    grande += f'Números encontrados: {len(cadenita)}'
    return grande

print(formato())


