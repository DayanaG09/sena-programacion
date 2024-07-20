class Piramide:
    def __init__(self):
        self.altura=None
        self.longitud=None
        self.ancho=None
        self.volumen=None        

##get datos
    def getAltura(self):
        return self.altura
    def getLongitud(self):
        return self.longitud
    def getAncho(self):
        return self.ancho
    def getVolumen(self):
        return self.volumen
    
    def guardarDatos(self, datos):
        self.Altura=datos[0]
        self.longitud=datos[1]
        self.ancho=datos[2]
        self.volumen=datos[3]
