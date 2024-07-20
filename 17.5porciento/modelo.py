class Operacion:
    def __init__(self):
        self.num1=None
        self.suma=None        

##get datos
    def getNum1(self):
        return self.num1
    def getSuma(self):
        return self.suma
    
    def guardarDatos(self, datos):
        self.num1=datos[0]
        self.suma=datos[1]
