import tkinter as   tk
from areaTrianguloModelo import Triangulo
from areaTrianguloControlador import ControllerArea
from areaTrianguloVista import VistaTriangulo
interfazPrincipal= tk.Tk()
objVista=VistaTriangulo(interfazPrincipal)
objModelo=Triangulo()
objControlador=ControllerArea(objVista, objModelo)
objVista.obtenerDatos()   
interfazPrincipal.mainloop()    
        
    
