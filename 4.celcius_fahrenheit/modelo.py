class Temperatura:
    def __init__(self):
        self.celsius=None
        self.cambio=None        

##get datos
    def getCelsius(self):
        return self.celsius
    def getCambio(self):
        return self.cambio
    
    def guardarDatos(self, datos):
        self.celsius=datos[0]
        self.cambio=datos[1]
        
