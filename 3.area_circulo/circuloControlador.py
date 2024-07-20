
from circuloModelo import Circulo
from circuloVista import VistaCirculo

class ControllerArea:
    def __init__(self, objvista,objModelo):
        self.objVista= objvista
        self.objModelo= objModelo
        self.objVista.controlador(self)
        
    def procesamientoDatos(self, datos):
        radio=int(datos[0])
        area=(3.1416*(radio * 2))
        datos=[radio,area]
        self.objModelo.guardarDatos(datos)
        self.mostrarDatos()
        return True
    
    def mostrarDatos(self):
        auxRadio=self.objModelo.getRadio()
        auxarea=self.objModelo.getArea()
        resultados=[auxRadio,auxarea]
        self.objVista.mostrarDatos(resultados)
        