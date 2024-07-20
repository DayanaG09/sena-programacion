class Trapecio:
    def __init__(self):
        self.altura=None
        self.baseSuper=None
        self.baseInfer=None
        self.area=None        

##get datos
    def getAltura(self):
        return self.altura
    def getBaseSuper(self):
        return self.baseSuper
    def getBaseInfer(self):
        return self.baseInfer
    def getArea(self):
        return self.area
    
    def guardarDatos(self, datos):
        self.Altura=datos[0]
        self.baseSuper=datos[1]
        self.baseInfer=datos[2]
        self.area=datos[3]
