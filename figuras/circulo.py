from figuras import figura
class circulo(figura):
    def __init__ (self, color, diametro):
        super().__init__(color)
        self.diametro = diametro
    def __str__ (self):
        return ("Se ha creado un circulo de color {}".format(self.color) + " con un diametro de {}".format(self.diametro))

