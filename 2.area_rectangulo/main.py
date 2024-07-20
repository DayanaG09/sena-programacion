import tkinter as   tk
from arearectanguloModelo import Rectangulo
from controladorAreaRectangulo import ControllerArea
from areaRectanguloVista import VistaRectangulo
interfazPrincipal= tk.Tk()
objVista=VistaRectangulo(interfazPrincipal)
objModelo=Rectangulo()
objControlador=ControllerArea(objVista, objModelo)
objVista.obtenerDatos()   
interfazPrincipal.mainloop()    
        
    
