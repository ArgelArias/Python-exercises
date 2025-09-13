import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio**2)

    def peri(self):
        return 2 * math.pi * self.radio

mi_circulo = Circulo(5)
print('El area del circulo es :', round(mi_circulo.area(), 2))
print('El perimetro del circulo es :', round(mi_circulo.peri(), 2))
