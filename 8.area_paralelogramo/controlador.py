from modelo import Paralelogramo
from vista import Vista

class ControllerArea:
    def __init__(self, objvista,objModelo):
        self.objVista= objvista
        self.objModelo= objModelo
        self.objVista.controlador(self)
        
    def procesamientoDatos(self, datos):
        altura=int(datos[0])
        base=int(datos[1])
        area=((base*altura)/2)
        datos=[altura,base,area]
        self.objModelo.guardarDatos(datos)
        self.mostrarDatos()
        return True
    
    def mostrarDatos(self):
        auxaltura=self.objModelo.getAltura()
        auxbase=self.objModelo.getBase()
        auxarea=self.objModelo.getArea()
        resultados=[auxaltura,auxbase,auxarea]
        self.objVista.mostrarDatos(resultados)
        