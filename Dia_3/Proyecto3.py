poema = input("Ingrese el poema: ").lower()
var = input("Ingrese las tres lestra en una sola cadena: ").lower()
palabras = var.split()
cant1 = poema.count(palabras[0])
cant2 = poema.count(palabras[1])
cant3 = poema.count(palabras[2])
booleano = "python" in poema
print(f"La letra {palabras[0]} se repite: {cant1} \n"
      f"La letra {palabras[1]} se repite: {cant2} \n"
      f"La letra {palabras[2]} se repite: {cant3} \n"
      f"El texto contiene un total de {len(poema)} caracteres \n"
      f"La última y primera letra del poema son {poema[0]} - {poema[len(poema) - 1]} respectivamente \n"
      f"El pomera en orden inverso es: {poema[::-1]} \n"
      f"Aparece python: {booleano}")
