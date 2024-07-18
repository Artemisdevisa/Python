import collections

# Escribe un programa que cuente la cantidad de veces que aparece cada palabra en un texto dado

texto = "hola mundo hola mundo mundo"
print(collections.Counter(texto.split()).most_common(1))