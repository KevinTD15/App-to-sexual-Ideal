class Postura: #en talla
    def __init__(self,datos):
        self.nombre = datos[0].get()
        self.placer = datos[1].get()
        self.agotamiento = datos[2].get()

        if self.placer == '':   self.placer=0
        if self.agotamiento == '':   self.agotamiento=0