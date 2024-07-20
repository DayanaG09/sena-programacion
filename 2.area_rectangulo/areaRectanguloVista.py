import tkinter as tk
from tkinter import messagebox

class VistaRectangulo:
    def __init__(self, interfazPrincipal):
        self.longitud=None
        self.ancho=None
        self.ventana= interfazPrincipal
       
        
    def obtenerDatos(self):
        self.ventana.title("CALCULADOR DE AREA DEL RECTANGULO")
        self.ventana.geometry("700x800")
        self.ventana.config(bg= "white", height=500, width=500 ) 
        labeldescripcion=tk.Label(self.ventana, text="ESTE PROGRAMA ESTA DISEÑADO PARA CALCULAR EL AREA DEL RECTANGULO", font=("Comic Sans MS", 12))
        labeldescripcion.config(bg="white")
        labeldescripcion.pack(pady=10)
        ##label Ancho
        labelAncho=tk.Label(self.ventana, text="Ingresa la Longitud para calcular el area del rectangulo\n ", font=("Comic Sans MS", 15))
        labelAncho.config(bg="#ff9078", relief="raised")
        labelAncho.pack(pady=10)
        ##entry ancho
        self.ancho=tk.Entry(self.ventana)
        self.ancho.pack(pady=10)
        #label longitud
        labellongitud=tk.Label(self.ventana, text="Ingresa el ancho  para calcular el area del rectangulo \n", font=("Comic Sans MS", 15))
        labellongitud.config(bg="#ff9078", relief="raised")
        labellongitud.pack(pady=10)
        ##entry longitud
        self.longitud=tk.Entry(self.ventana)
        self.longitud.pack(pady=10)
        
        self.buttonCalculador=tk.Button(self.ventana, text="CALCULAR", command=self.verificarDatos)
        self.buttonCalculador.config(bg="#d66d58", relief="raised")
        self.buttonCalculador.pack(pady=10)
        return self.ventana
    def controlador(self,Controlador):
        self.controlador=Controlador
    def verificarDatos(self):
        if not self.longitud.get() or not self.ancho.get():
            messagebox.showerror("Error")
        else: 
            if self.longitud.get().isdigit() and self.ancho.get().isdigit():
                calcularDatos=[self.longitud.get(), self.ancho.get()]
                self.controlador.procesamientoDatos(calcularDatos)  
            else:
                messagebox.showerror("error, numeros ingresados no validos para ejecutar la operacion") 
                
#Utilice isdigit para comprobar si el nuevo valor es un número o si el campo está vacío (permitiendo la eliminación de caracteres).
    def mostrarDatos(self, area):
        self.buttonCalculador.config(state="disabled")
        labelRta=tk.Label(self.ventana, text=f"El area de triangulo es:{area[2]} metros cubicos")
        labelRta.config(bg="#b89527", relief="raised")
        labelRta.pack(pady=10)