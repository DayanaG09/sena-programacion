import tkinter as   tk
from modelo import Operacion
from controlador import Controller
from vista import VistaOperacion
interfazPrincipal= tk.Tk()
objVista=VistaOperacion(interfazPrincipal)
objModelo=Operacion()
objControlador=Controller(objVista, objModelo)
objVista.obtenerDatos()   
interfazPrincipal.mainloop()    
        
    
