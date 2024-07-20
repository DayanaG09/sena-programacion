import tkinter as   tk
from modelo import Kilogramos
from controlador import Controller
from vista import VistaKg
interfazPrincipal= tk.Tk()
objVista=VistaKg(interfazPrincipal)
objModelo=Kilogramos()
objControlador=Controller(objVista, objModelo)
objVista.obtenerDatos()   
interfazPrincipal.mainloop()    
        
    
