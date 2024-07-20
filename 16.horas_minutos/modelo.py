class operacion:
    def __init__(self):
        self.num=None
        self.rta=None        

##get datos
    def getNum(self):
        return self.num
    def getRta(self):
        return self.rta
    
    def guardarDatos(self, datos):
        self.num=datos[0]
        self.rta=datos[1]