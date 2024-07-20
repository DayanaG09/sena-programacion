import tkinter as tk
from tkinter import messagebox

class VistaMillas:
    def __init__(self, interfazPrincipal):
        self.km=None
        self.ventana= interfazPrincipal
       
        
    def obtenerDatos(self):
        self.ventana.title("CALCULADOR DE KM A MILLAS")
        self.ventana.geometry("700x800")
        self.ventana.config(bg= "#e8fdff", height=500, width=500 ) 
        labeldescripcion=tk.Label(self.ventana, text="ESTE PROGRAMA ESTA DISEÑADO PARA CONVERTIR KM A MILLAS", font=("Comic Sans MS", 12))
        labeldescripcion.config(bg="#e8fdff")
        labeldescripcion.pack(pady=10)
        labeldescripcion=tk.Label(self.ventana, text="A continuacion ingresa los valores que se requieren ", font=("Comic Sans MS", 12))
        labeldescripcion.config(bg="#e8fdff")
        labeldescripcion.pack(pady=10)
        ##label km
        labelkm=tk.Label(self.ventana, text="Ingresa los kilometros para convertir a millas \n", font=("Comic Sans MS", 15))
        labelkm.config(bg="#a69785", relief="raised")
        labelkm.pack(pady=10)
        ##entry km
        self.km=tk.Entry(self.ventana)
        self.km.pack(pady=10)
        
        self.buttonCalculador=tk.Button(self.ventana, text="CONVERTIR", command=self.verificarDatos)
        self.buttonCalculador.config(bg="#a69785", relief="raised")
        self.buttonCalculador.pack(pady=10)
        return self.ventana
    def controlador(self,Controlador):
        self.controlador=Controlador
    def verificarDatos(self):
        if not self.km.get() :
            messagebox.showerror("Error")
        else: 
            if self.km.get().isdigit() :
                calcularDatos=[self.km.get()]
                self.controlador.procesamientoDatos(calcularDatos)  
            else:
                messagebox.showerror("error, numeros ingresados no validos para ejecutar la operacion") 
                
#Utilice isdigit para comprobar si el nuevo valor es un número o si el campo está vacío (permitiendo la eliminación de caracteres).
    def mostrarDatos(self, millas):
        self.buttonCalculador.config(state="disabled")
        labelRta=tk.Label(self.ventana, text=f"El area del circulo es :{millas[1]}", font=("Comic Sans MS", 15) )
        labelRta.config(bg="#eee9e5", relief="raised")
        labelRta.pack(pady=10)