import tkinter as   tk
from modelo import Piramide
from controlador import Controller
from vista import VistaPiramide
interfazPrincipal= tk.Tk()
objVista=VistaPiramide(interfazPrincipal)
objModelo=Piramide()
objControlador=Controller(objVista, objModelo)
objVista.obtenerDatos()   
interfazPrincipal.mainloop()    
        
    
