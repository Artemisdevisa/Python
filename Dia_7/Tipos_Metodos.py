class Pajaro:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    def piar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color="negro"
        print(f"Ahora el pajara es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        print(f"Tienes alas= {cls.alas}")
    @staticmethod
    def mirar():


piolon = Pajaro("amarillo", "canario")
piolon.volar(100)
Pajaro.poner_huevos(3)