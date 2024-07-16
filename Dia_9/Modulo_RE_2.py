import re

'''Patrones con expresiones regulares'''
texto = "llama al 564-527-6588 ya mismo"

patron = r'\d{3}-\d{3}-\d{4}'

resultado = re.search(patron, texto)
'''Muestra el resultado'''
print(resultado)
'''Obtener el numero econtrado segun el patron'''
print(resultado.group())

'''USOS PRÁCTICOS'''

'''clave = input("Clave: ")

chequear = re.search(patron, clave)
print(chequear)'''

'''Bucar dos palabras por el o  -> |'''
texto = "No atendemos los lunes por la tarde"
buscar = re.search(r'lunes|martes', texto)
print(buscar)
