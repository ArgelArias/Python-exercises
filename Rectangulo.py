class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

my_rect = Rectangulo(5,3)
print('El area del rectangulo es :', my_rect.area())
