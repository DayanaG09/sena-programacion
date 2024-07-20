import tkinter as tk
from tkinter import messagebox

class VistaOperacion:
    def __init__(self, interfazPrincipal):
        self.num1=None
        self.num2=None
        self.ventana= interfazPrincipal
       
        
    def obtenerDatos(self):
        self.ventana.title("RAIZ CUADRADA")
        self.ventana.geometry("700x800")
        self.ventana.config(bg= "#ffd1b3", height=500, width=500 ) 
        labeldescripcion=tk.Label(self.ventana, text="ESTE PROGRAMA ESTA DISEÑADO PARA CALCULAR LA RAIZ CUADRADA", font=("Comic Sans MS", 15))
        labeldescripcion.config(bg="#ffd1b3")
        labeldescripcion.pack(pady=10)
        ##label PRIMER NUM
        label1=tk.Label(self.ventana, text="Ingresa el numero que deseas sacarle raiz cuadrada:  \n", font=("Comic Sans MS", 15))
        label1.config(bg="#e8e7d2", relief="raised")
        label1.pack(pady=10)
        ##entry PRIMER NUM
        self.num1=tk.Entry(self.ventana)
        self.num1.pack(pady=10)
        
        self.buttonCalculador=tk.Button(self.ventana, text="Calcular", command=self.verificarDatos)
        self.buttonCalculador.config(bg="#e8e7d2", relief="raised")
        self.buttonCalculador.pack(pady=10)
        return self.ventana
    def controlador(self,Controlador):
        self.controlador=Controlador
    def verificarDatos(self):
        if not self.num1.get() :
            messagebox.showerror("Error")
        else: 
            if self.num1.get().isdigit():
                calcularDatos=[self.num1.get()]
                self.controlador.procesamientoDatos(calcularDatos)  
            else:
                messagebox.showerror("error, numeros ingresados no validos para ejecutar la operacion") 
                
#Utilice isdigit para comprobar si el nuevo valor es un número o si el campo está vacío (permitiendo la eliminación de caracteres).
    def mostrarDatos(self, rta):
        self.buttonCalculador.config(state="disabled")
        labelRta=tk.Label(self.ventana, text=f"EL 5%  es:   {rta[1]}")
        labelRta.config(bg="#deddc4", relief="raised")
        labelRta.pack(pady=10)