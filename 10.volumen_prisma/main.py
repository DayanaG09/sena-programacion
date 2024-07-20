import tkinter as   tk
from modelo import Prisma
from controlador import Controller
from vista import VistaPrisma
interfazPrincipal= tk.Tk()
objVista=VistaPrisma(interfazPrincipal)
objModelo=Prisma()
objControlador=Controller(objVista, objModelo)
objVista.obtenerDatos()   
interfazPrincipal.mainloop()    
        
    