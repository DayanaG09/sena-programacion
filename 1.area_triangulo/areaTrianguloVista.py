import tkinter as tk
from tkinter import messagebox

class VistaTriangulo:
    def __init__(self, interfazPrincipal):
        self.altura=None
        self.base=None
        self.ventana= interfazPrincipal
       
        
    def obtenerDatos(self):
        self.ventana.title("CALCULADOR DE AREA DEL TRIANGULO")
        self.ventana.geometry("700x800")
        self.ventana.config(bg= "#718ead", height=500, width=500 ) 
        labeldescripcion=tk.Label(self.ventana, text="ESTE PROGRAMA ESTA DISEÑADO PARA CALCULAR EL AREA DEL TRIANGULO", font=("Comic Sans MS", 15))
        labeldescripcion.config(bg="#718ead")
        labeldescripcion.pack(pady=10)
        ##label ALTURA
        labelAltura=tk.Label(self.ventana, text="ingresa la altura para calcular el area\n", font=("Comic Sans MS", 15))
        labelAltura.config(bg="#a2c0d6", relief="raised")
        labelAltura.pack(pady=10)
        ##entry altura
        self.altura=tk.Entry(self.ventana)
        self.altura.pack(pady=10)
        #label Base
        labelBase=tk.Label(self.ventana, text="ingresa la base para calcular el area\n", font=("Comic Sans MS", 15))
        labelBase.config(bg="#a2c0d6", relief="raised")
        labelBase.pack(pady=10)
        ##entry base
        self.base=tk.Entry(self.ventana)
        self.base.pack(pady=10)
        
        self.buttonCalculador=tk.Button(self.ventana, text="Calcular", command=self.verificarDatos)
        self.buttonCalculador.config(bg="#8b96be", relief="raised")
        self.buttonCalculador.pack(pady=10)
        return self.ventana
    def controlador(self,Controlador):
        self.controlador=Controlador
    def verificarDatos(self):
        if not self.base.get() or not self.altura.get():
            messagebox.showerror("Error")
        else: 
            if self.base.get().isdigit() and self.altura.get().isdigit():
                calcularDatos=[self.base.get(), self.altura.get()]
                self.controlador.procesamientoDatos(calcularDatos)  
            else:
                messagebox.showerror("error, numeros ingresados no validos para ejecutar la operacion") 
                
#Utilice isdigit para comprobar si el nuevo valor es un número o si el campo está vacío (permitiendo la eliminación de caracteres).
    def mostrarDatos(self, area):
        self.buttonCalculador.config(state="disabled")
        labelRta=tk.Label(self.ventana, text=f"El area de triangulo es:{area[2]}")
        labelRta.config(bg="#f6d1d9", relief="raised")
        labelRta.pack(pady=10)