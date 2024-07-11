lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

lista = list(enumerate(lista_nombres))

for val in lista:
    if val[1].startswith("M"):
        print(val[0])
