from modelo import Trapecio
from vista import VistaTrapecio

class ControllerArea:
    def __init__(self, objvista,objModelo):
        self.objVista= objvista
        self.objModelo= objModelo
        self.objVista.controlador(self)
        
    def procesamientoDatos(self, datos):
        altura=int(datos[0])
        baseSuper=int(datos[1])
        baseInfer=int(datos[2])
        area=((baseInfer+baseSuper//2)*altura)
        datos=[altura,baseSuper, baseInfer,area]
        self.objModelo.guardarDatos(datos)
        self.mostrarDatos()
        return True
    
    def mostrarDatos(self):
        auxaltura=self.objModelo.getAltura()
        auxbaseSuper=self.objModelo.getBaseSuper()
        auxbaseInfer=self.objModelo.getBaseInfer()
        auxarea=self.objModelo.getArea()
        resultados=[auxaltura,auxbaseSuper,auxbaseInfer,auxarea]
        self.objVista.mostrarDatos(resultados)
        