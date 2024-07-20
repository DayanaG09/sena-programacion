class Millas:
    def __init__(self):
        self.km=None
        self.millas=None        

##get datos
    def getKm(self):
        return self.km
    def getMillas(self):
        return self.millas
    
    def guardarDatos(self, datos):
        self.km=datos[0]
        self.millas=datos[1]