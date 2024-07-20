class Paralelogramo:
    def __init__(self):
        self.altura=None
        self.base=None
        self.area=None        

##get datos
    def getAltura(self):
        return self.altura
    def getBase(self):
        return self.base
    def getArea(self):
        return self.area
    
    def guardarDatos(self, datos):
        self.Altura=datos[0]
        self.Base=datos[1]
        self.area=datos[2]
