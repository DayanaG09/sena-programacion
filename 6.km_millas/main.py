import tkinter as   tk
from modelo import Millas
from controlador import Controller
from vista import VistaMillas
interfazPrincipal= tk.Tk()
objVista=VistaMillas(interfazPrincipal)
objModelo=Millas()
objControlador=Controller(objVista, objModelo)
objVista.obtenerDatos()   
interfazPrincipal.mainloop()    
        
    
