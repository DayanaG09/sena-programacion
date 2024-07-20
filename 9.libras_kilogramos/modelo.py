class Kilogramos:
    def __init__(self):
        self.libras=None
        self.kg=None        

##get datos
    def getLibras(self):
        return self.libras
    def getKg(self):
        return self.kg
    
    def guardarDatos(self, datos):
        self.libras=datos[0]
        self.kg=datos[1]