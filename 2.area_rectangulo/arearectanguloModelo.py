class Rectangulo:
    def __init__(self):
        self.longitud=None
        self.ancho=None
        self.area=None        

##get datos
    def getLongitud(self):
        return self.longitud
    def getAncho(self):
        return self.ancho
    def getArea(self):
        return self.area
    
    def guardarDatos(self, datos):
        self.longitud=datos[0]
        self.ancho=datos[1]
        self.area=datos[2]
