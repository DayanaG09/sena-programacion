import tkinter as tk
from tkinter import messagebox

class VistaOperacion:
    def __init__(self, interfazPrincipal):
        self.num=None
        self.ventana= interfazPrincipal
       
        
    def obtenerDatos(self):
        self.ventana.title("PAR O IMPAR")
        self.ventana.geometry("700x800")
        self.ventana.config(bg= "#ae8fba", height=500, width=500 ) 
        labeldescripcion=tk.Label(self.ventana, text="ESTE PROGRAMA ESTA DISEÑADO PARA COMPROBAR SI UN NUMERO ES PAR O IMPAR", font=("Comic Sans MS", 12))
        labeldescripcion.config(bg="#ae8fba")
        labeldescripcion.pack(pady=10)
        labeldescripcion=tk.Label(self.ventana, text="A continuacion ingresa los valores que se requieren ", font=("Comic Sans MS", 12))
        labeldescripcion.config(bg="#ae8fba")
        labeldescripcion.pack(pady=10)
        ##label 
        label=tk.Label(self.ventana, text="Ingresa el numero que vas a comprobar \n", font=("Comic Sans MS", 15))
        label.config(bg="#f2e7d2", relief="raised")
        label.pack(pady=10)
        ##entry km
        self.num=tk.Entry(self.ventana)
        self.num.pack(pady=10)
        
        self.buttonCalculador=tk.Button(self.ventana, text="COMPROBAR", command=self.verificarDatos)
        self.buttonCalculador.config(bg="#f2e7d2", relief="raised")
        self.buttonCalculador.pack(pady=10)
        return self.ventana
    def controlador(self,Controlador):
        self.controlador=Controlador
    def verificarDatos(self):
        if not self.num.get() :
            messagebox.showerror("Error")
        else: 
            if self.num.get().isdigit() :
                calcularDatos=[self.num.get()]
                self.controlador.procesamientoDatos(calcularDatos)  
            else:
                messagebox.showerror("error, numeros ingresados no validos para ejecutar la operacion") 
                
#Utilice isdigit para comprobar si el nuevo valor es un número o si el campo está vacío (permitiendo la eliminación de caracteres).
    def mostrarDatos(self, rta):
        self.buttonCalculador.config(state="disabled")
        labelRta=tk.Label(self.ventana, text=f"{rta[1]}", font=("Comic Sans MS", 15) )
        labelRta.config(bg="#f2e7d2", relief="raised")
        labelRta.pack(pady=10)