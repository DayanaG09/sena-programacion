from modelo import Prisma
from vista import VistaPrisma

class Controller:
    def __init__(self, objvista,objModelo):
        self.objVista= objvista
        self.objModelo= objModelo
        self.objVista.controlador(self)
        
    def procesamientoDatos(self, datos):
        altura=int(datos[0])
        longitud=int(datos[1])
        ancho=int(datos[2])
        volumen=(longitud*ancho*altura)
        datos=[altura,longitud,ancho,volumen]
        self.objModelo.guardarDatos(datos)
        self.mostrarDatos()
        return True
    
    def mostrarDatos(self):
        auxaltura=self.objModelo.getAltura()
        auxLongitud=self.objModelo.getLongitud()
        auxAncho=self.objModelo.getAncho()
        auxVolumen=self.objModelo.getVolumen()
        resultados=[auxaltura,auxLongitud,auxAncho,auxVolumen]
        self.objVista.mostrarDatos(resultados)
        