import tkinter as tk
from tkinter import messagebox

class VistaKg:
    def __init__(self, interfazPrincipal):
        self.libras=None
        self.ventana= interfazPrincipal
       
        
    def obtenerDatos(self):
        self.ventana.title("CALCULADOR DE LIBRAS A KM")
        self.ventana.geometry("700x800")
        self.ventana.config(bg= "#e8fdff", height=500, width=500 ) 
        labeldescripcion=tk.Label(self.ventana, text="ESTE PROGRAMA ESTA DISEÑADO PARA CONVERTIR LIBRAS A KILOGRAMOS", font=("Comic Sans MS", 12))
        labeldescripcion.config(bg="#e8fdff")
        labeldescripcion.pack(pady=10)
        labeldescripcion=tk.Label(self.ventana, text="A continuacion ingresa los valores que se requieren ", font=("Comic Sans MS", 12))
        labeldescripcion.config(bg="#e8fdff")
        labeldescripcion.pack(pady=10)
        ##label libras
        labelLibras=tk.Label(self.ventana, text="Ingresa los kilometros para convertir a millas \n", font=("Comic Sans MS", 15))
        labelLibras.config(bg="#a69785", relief="raised")
        labelLibras.pack(pady=10)
        ##entry libras
        self.libras=tk.Entry(self.ventana)
        self.libras.pack(pady=10)
        
        self.buttonCalculador=tk.Button(self.ventana, text="CONVERTIR", command=self.verificarDatos)
        self.buttonCalculador.config(bg="#a69785", relief="raised")
        self.buttonCalculador.pack(pady=10)
        return self.ventana
    def controlador(self,Controlador):
        self.controlador=Controlador
    def verificarDatos(self):
        if not self.libras.get() :
            messagebox.showerror("Error")
        else: 
            if self.libras.get().isdigit() :
                calcularDatos=[self.libras.get()]
                self.controlador.procesamientoDatos(calcularDatos)  
            else:
                messagebox.showerror("error, numeros ingresados no validos para ejecutar la operacion") 
                
#Utilice isdigit para comprobar si el nuevo valor es un número o si el campo está vacío (permitiendo la eliminación de caracteres).
    def mostrarDatos(self, kg):
        self.buttonCalculador.config(state="disabled")
        labelRta=tk.Label(self.ventana, text=f"El area del circulo es :{kg[1]}", font=("Comic Sans MS", 15) )
        labelRta.config(bg="#eee9e5", relief="raised")
        labelRta.pack(pady=10)