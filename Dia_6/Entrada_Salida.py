mi_archivo = open('Prueba.txt')

todas = mi_archivo.readlines()
todas = todas.pop()
print(todas)

mi_archivo.close()
