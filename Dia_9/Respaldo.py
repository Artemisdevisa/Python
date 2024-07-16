import os

ruta = "C:\\Users\\jenny\\Desktop\\Mi_Gran_Directorio"

for carpeta, subcarpeta, archivos in os.walk(ruta):
    for arch in archivos:
        print(subcarpeta)
    for sub in subcarpeta:
        print(sub)