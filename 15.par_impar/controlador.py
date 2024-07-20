
from modelo import Operacion
from vista import VistaOperacion

class Controller:
    def __init__(self, objvista,objModelo):
        self.objVista= objvista
        self.objModelo= objModelo
        self.objVista.controlador(self)
        
    def procesamientoDatos(self, datos):
        num=int(datos[0]) 
        if num % 2== 0:
            rta="EL NUMERO ES PAR"
        else:
            rta="EL NUMERO ES IMPAR"
        datos=[num, rta]
        self.objModelo.guardarDatos(datos)
        self.mostrarDatos()
        return True
    
    def mostrarDatos(self):
        auxNum=self.objModelo.getNum()
        auxRta=self.objModelo.getRta()
        resultados=[auxNum,auxRta]
        self.objVista.mostrarDatos(resultados)
        