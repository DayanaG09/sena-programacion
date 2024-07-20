import tkinter as tk
from tkinter import messagebox

class VistaTemperatura:
    def __init__(self, interfazPrincipal):
        self.celsius=None
        self.ventana= interfazPrincipal
       
        
    def obtenerDatos(self):
        self.ventana.title("-----------CONVERTIDOR DE TEMPPERATURA--------------")
        self.ventana.geometry("700x800")
        self.ventana.config(bg= "#f7dece", height=500, width=500 ) 
        labeldescripcion=tk.Label(self.ventana, text="CONVERTIDOR DE TEMPERATURA", font=("Comic Sans MS", 12))
        labeldescripcion.config(bg="#f7dece")
        labeldescripcion.pack(pady=10)
        labeldescripcion=tk.Label(self.ventana, text="Este programa esta diseñado para que ingreses \n los grados celcius y se convertiran a grados fahrenheit", font=("Comic Sans MS", 12))
        labeldescripcion.config(bg="#f7dece")
        labeldescripcion.pack(pady=10)
        ##label celsius
        labelCelsius=tk.Label(self.ventana, text="Ingresa los grados celsius  \n", font=("Comic Sans MS", 15))
        labelCelsius.config(bg="#9ec4bb", relief="raised")
        labelCelsius.pack(pady=10)
        ##entry celsius
        self.celsius=tk.Entry(self.ventana)
        self.celsius.pack(pady=10)
        
        self.buttonCalculador=tk.Button(self.ventana, text="CONVERTIR", bg="black", command=self.verificarDatos)
        self.buttonCalculador.config(bg="#ccccbb", relief="raised")
        self.buttonCalculador.pack(pady=10)
        return self.ventana
    def controlador(self,Controlador):
        self.controlador=Controlador
    def verificarDatos(self):
        if not self.celsius.get() :
            messagebox.showerror("Error")
        else: 
            if self.celsius.get().isdigit() :
                calcularDatos=[self.celsius.get()]
                self.controlador.procesamientoDatos(calcularDatos)  
            else:
                messagebox.showerror("error, numeros ingresados no validos para ejecutar la operacion") 
                
    def mostrarDatos(self, cambio):
        self.buttonCalculador.config(state="disabled")
        labelRta=tk.Label(self.ventana, text=f"La temperatura es:{cambio[1]} grados fahrenheit")
        labelRta.config(bg="#f6d1d9", relief="raised")
        labelRta.pack(pady=10)