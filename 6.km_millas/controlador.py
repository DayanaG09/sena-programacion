
from modelo import Millas
from vista import VistaMillas

class Controller:
    def __init__(self, objvista,objModelo):
        self.objVista= objvista
        self.objModelo= objModelo
        self.objVista.controlador(self)
        
    def procesamientoDatos(self, datos):
        km=int(datos[0])
        millas=(km*0.621)
        datos=[km,millas]
        self.objModelo.guardarDatos(datos)
        self.mostrarDatos()
        return True
    
    def mostrarDatos(self):
        auxkm=self.objModelo.getKm()
        auxmillas=self.objModelo.getMillas()
        resultados=[auxkm,auxmillas]
        self.objVista.mostrarDatos(resultados)
        