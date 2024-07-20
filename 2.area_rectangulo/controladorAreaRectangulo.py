from arearectanguloModelo import Rectangulo
from areaRectanguloVista import VistaRectangulo

class ControllerArea:
    def __init__(self, objvista,objModelo):
        self.objVista= objvista
        self.objModelo= objModelo
        self.objVista.controlador(self)
        
    def procesamientoDatos(self, datos):
        longitud=int(datos[0])
        ancho=int(datos[1])
        area=(longitud*ancho)
        datos=[ancho,longitud,area]
        self.objModelo.guardarDatos(datos)
        self.mostrarDatos()
        return True
    
    def mostrarDatos(self):
        auxAncho=self.objModelo.getAncho()
        auxLongitud=self.objModelo.getLongitud()
        auxarea=self.objModelo.getArea()
        resultados=[auxAncho,auxLongitud,auxarea]
        self.objVista.mostrarDatos(resultados)
        