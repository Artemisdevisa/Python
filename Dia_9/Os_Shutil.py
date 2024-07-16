import shutil
import os

'''Crear el árbol con os.walk y un iterador'''
'''En los iteradores al ser string se pueden aplicar metodos de las mismas'''

ruta = "C:\\Users\\jenny\\Desktop\\VISA_MAYOR"

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"El nombre de la carpeta es: {carpeta}")
    for sub in subcarpeta:
        print(f"Su subcarpeta es: {sub}")
    for arh in archivo:
        print(f'Su archivo es: {arh}')
        print("\n")

