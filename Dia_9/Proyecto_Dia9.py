import os
grande = ""
cadenita = []
ruta = "C:\\Users\\jenny\\Desktop\\Mi_Gran_Directorio"
'''------------------------------------------------------------------------------------------'''
os.chdir(f"C:\\Users\\jenny\\Desktop\\Mi_Gran_Directorio")
def lectura(ruta):
    for carpeta, subcarpeta, archivos in os.walk(ruta):
        print(carpeta)
        for sub in subcarpeta:
            print(sub)
        for arch in archivos:
                print(arch)


lectura(ruta)

def formato():
    grande = ("ARCHIVO\t\t\t\tNRO.SERIE\n"
              "-------\t\t\t\t----------\n")
    for val in cadenita:
        grande += f"{val.split("-")[0]}\t\t\t\t{val.split("-")[1]}\n"

    return grande


