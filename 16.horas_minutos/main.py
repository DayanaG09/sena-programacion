import tkinter as   tk
from modelo import operacion
from controlador import Controller
from vista import VistaOperacion
interfazPrincipal= tk.Tk()
objVista=VistaOperacion(interfazPrincipal)
objModelo=operacion()
objControlador=Controller(objVista, objModelo)
objVista.obtenerDatos()   
interfazPrincipal.mainloop()    
        
    
