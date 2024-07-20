
from modelo import Kilogramos
from vista import VistaKg

class Controller:
    def __init__(self, objvista,objModelo):
        self.objVista= objvista
        self.objModelo= objModelo
        self.objVista.controlador(self)
        
    def procesamientoDatos(self, datos):
        libras=int(datos[0])
        kg=(km*0.621)
        datos=[libras,kg]
        self.objModelo.guardarDatos(datos)
        self.mostrarDatos()
        return True
    
    def mostrarDatos(self):
        auxLibras=self.objModelo.getLibras()
        auxKg=self.objModelo.getKg()
        resultados=[getLibras,getKg]
        self.objVista.mostrarDatos(resultados)
        