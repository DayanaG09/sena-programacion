import tkinter as tk
from tkinter import messagebox

class VistaCirculo:
    def __init__(self, interfazPrincipal):
        self.radio=None
        self.ventana= interfazPrincipal
       
        
    def obtenerDatos(self):
        self.ventana.title("CALCULADOR DE AREA DEL TRIANGULO")
        self.ventana.geometry("700x800")
        self.ventana.config(bg= "#ffba7f", height=500, width=500 ) 
        labeldescripcion=tk.Label(self.ventana, text="ESTE PROGRAMA ESTA DISEÑADO PARA CALCULAR EL AREA DEL CIRCULO", font=("Comic Sans MS", 12))
        labeldescripcion.config(bg="#ffba7f")
        labeldescripcion.pack(pady=10)
        labeldescripcion=tk.Label(self.ventana, text="A continuacion ingresa los valores que se requieren ", font=("Comic Sans MS", 12))
        labeldescripcion.config(bg="#ffba7f")
        labeldescripcion.pack(pady=10)
        ##label radio
        labelRadio=tk.Label(self.ventana, text="Ingresa el radio para calcular el area del circulo \n", font=("Comic Sans MS", 15))
        labelRadio.config(bg="#eee9e5", relief="raised")
        labelRadio.pack(pady=10)
        ##entry radio
        self.radio=tk.Entry(self.ventana)
        self.radio.pack(pady=10)
        
        self.buttonCalculador=tk.Button(self.ventana, text="CALCULAR", command=self.verificarDatos)
        self.buttonCalculador.config(bg="#ffe181", relief="raised")
        self.buttonCalculador.pack(pady=10)
        return self.ventana
    def controlador(self,Controlador):
        self.controlador=Controlador
    def verificarDatos(self):
        if not self.radio.get() :
            messagebox.showerror("Error")
        else: 
            if self.radio.get().isdigit() :
                calcularDatos=[self.radio.get()]
                self.controlador.procesamientoDatos(calcularDatos)  
            else:
                messagebox.showerror("error, numeros ingresados no validos para ejecutar la operacion") 
                
#Utilice isdigit para comprobar si el nuevo valor es un número o si el campo está vacío (permitiendo la eliminación de caracteres).
    def mostrarDatos(self, area):
        self.buttonCalculador.config(state="disabled")
        labelRta=tk.Label(self.ventana, text=f"El area del circulo es :{area[1]}", font=("Comic Sans MS", 15) )
        labelRta.config(bg="#eee9e5", relief="raised")
        labelRta.pack(pady=10)