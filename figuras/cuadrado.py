from figuras import figura
class cuadrado(figura):
    def __init__ (self, color, lado):
        super().__init__(color)
        self.lado = lado
    def __str__(self):
        return ("El color del cuadrado es {}".format(self.color) + "El lado del cuadrado es {}".format(self.lado))
        