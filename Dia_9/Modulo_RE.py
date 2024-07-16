import re

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

palabra = 'ayuda' in texto
print(palabra)

patron = 'ayuda'

'''busco por expresiones regulares'''
busqueda = re.search(patron, texto)
print(busqueda)
'''obtengo el indice de inicio'''
print(busqueda.start())
'''obtengo el indice de fin'''
print(busqueda.end())

busqueda = re.findall(patron, texto)
'''obtengo una lista con las palabras encontradas'''
print(busqueda)
'''obtengo cuantas veces se repite dicha palabra'''
print(len(busqueda))