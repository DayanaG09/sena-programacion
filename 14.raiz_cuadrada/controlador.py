from modelo import Operacion
from vista import VistaOperacion
from math import sqrt

class Controller:
    def __init__(self, objvista,objModelo):
        self.objVista= objvista
        self.objModelo= objModelo
        self.objVista.controlador(self)
        
    def procesamientoDatos(self, datos):
        numero1=int(datos[0])
        raiz=int(sqrt(numero1))
        datos=[numero1,raiz]
        self.objModelo.guardarDatos(datos)
        self.mostrarDatos()
        return True
    
    def mostrarDatos(self):
        auxNum1=self.objModelo.getNum1()
        auxSuma=self.objModelo.getSuma()
        resultados=[auxNum1,auxSuma]
        self.objVista.mostrarDatos(resultados)
        