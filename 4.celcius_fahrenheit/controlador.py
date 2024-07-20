
from modelo import Temperatura
from vista import VistaTemperatura

class Controller:
    def __init__(self, objvista,objModelo):
        self.objVista= objvista
        self.objModelo= objModelo
        self.objVista.controlador(self)
        
    def procesamientoDatos(self, datos):
        celsius=int(datos[0])
        cambio=(celsius * 9/5)+32
        datos=[celsius, cambio]
        self.objModelo.guardarDatos(datos)
        self.mostrarDatos()
        return True
    
    def mostrarDatos(self):
        auxCelsius=self.objModelo.getCelsius()
        auxCambio=self.objModelo.getCambio()
        resultados=[auxCelsius,auxCambio]
        self.objVista.mostrarDatos(resultados)
        