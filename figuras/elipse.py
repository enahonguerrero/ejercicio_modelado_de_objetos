from figuras import figura
class elipse(figura):
    def __init__(self, color, foco ):
        super().__init__(color)
        self.foco = foco
    def __str__(self):
        return ("El color de la elipse es{}".format(self.color) + "El foco de la elipse es{}".format(self.foco))
    
    