import tkinter as   tk
from circuloModelo import Circulo
from circuloControlador import ControllerArea
from circuloVista import VistaCirculo
interfazPrincipal= tk.Tk()
objVista=VistaCirculo(interfazPrincipal)
objModelo=Circulo()
objControlador=ControllerArea(objVista, objModelo)
objVista.obtenerDatos()   
interfazPrincipal.mainloop()    
        
    
