class Operacion:
    def __init__(self):
        self.num1=None
        self.num2=None
        self.suma=None        

##get datos
    def getNum1(self):
        return self.num1
    def getNum2(self):
        return self.num2
    def getSuma(self):
        return self.suma
    
    def guardarDatos(self, datos):
        self.num1=datos[0]
        self.num2=datos[1]
        self.suma=datos[2]
