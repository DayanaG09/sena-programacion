import tkinter as   tk
from modelo import Paralelogramo
from controlador import ControllerArea
from vista import Vista
interfazPrincipal= tk.Tk()
objVista=Vista(interfazPrincipal)
objModelo=Paralelogramo()
objControlador=ControllerArea(objVista, objModelo)
objVista.obtenerDatos()   
interfazPrincipal.mainloop()    
        
    
