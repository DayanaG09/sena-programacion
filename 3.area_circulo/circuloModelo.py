class Circulo:
    def __init__(self):
        self.radio=None
        self.area=None        

##get datos
    def getRadio(self):
        return self.radio
    def getArea(self):
        return self.area
    
    def guardarDatos(self, datos):
        self.radio=datos[0]
        self.area=datos[1]
        
