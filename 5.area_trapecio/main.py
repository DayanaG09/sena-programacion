import tkinter as   tk
from modelo import Trapecio
from controlador import ControllerArea
from vista import VistaTrapecio
interfazPrincipal= tk.Tk()
objVista=VistaTrapecio(interfazPrincipal)
objModelo=Trapecio()
objControlador=ControllerArea(objVista, objModelo)
objVista.obtenerDatos()   
interfazPrincipal.mainloop()    
        
    
