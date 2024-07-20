from modelo import Operacion
from vista import VistaOperacion

class Controller:
    def __init__(self, objvista,objModelo):
        self.objVista= objvista
        self.objModelo= objModelo
        self.objVista.controlador(self)
        
    def procesamientoDatos(self, datos):
        numero1=int(datos[0])
        numero2=int(datos[1])
        if numero1 % numero2==0:
            rta=f"EL {numero1} es multiplo de {numero2}"
        else:
            rta=f"EL {numero1} no es multiplo de {numero2}"

        datos=[numero1, numero2, rta]
        self.objModelo.guardarDatos(datos)
        self.mostrarDatos()
        return True
    
    def mostrarDatos(self):
        auxNum1=self.objModelo.getNum1()
        auxNum2=self.objModelo.getNum2()
        auxSuma=self.objModelo.getSuma()
        resultados=[auxNum1,auxNum2,auxSuma]
        self.objVista.mostrarDatos(resultados)
        