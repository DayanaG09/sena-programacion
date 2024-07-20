import tkinter as   tk
from modelo import Temperatura
from controlador import Controller
from vista import VistaTemperatura
interfazPrincipal= tk.Tk()
objVista=VistaTemperatura(interfazPrincipal)
objModelo=Temperatura()
objControlador=Controller(objVista, objModelo)
objVista.obtenerDatos()   
interfazPrincipal.mainloop()    
        
    
