import tkinter as tk
from tkinter import messagebox

class VistaTrapecio:
    def __init__(self, interfazPrincipal):
        self.altura=None
        self.baseSuper=None
        self.baseInfer=None
        self.ventana= interfazPrincipal
       
        
    def obtenerDatos(self):
        self.ventana.title("CALCULADOR DE AREA DEL TRAPECIO")
        self.ventana.geometry("700x800")
        self.ventana.config(bg= "#add6bc", height=500, width=500 ) 
        labeldescripcion=tk.Label(self.ventana, text="ESTE PROGRAMA ESTA DISEÑADO PARA CALCULAR EL AREA DEL TRAPECIO", font=("Comic Sans MS", 15))
        labeldescripcion.config(bg="#add6bc")
        labeldescripcion.pack(pady=10)
        labeldescripcion=tk.Label(self.ventana, text="A continuación ingresa los datos que te solicitan\n ", font=("Comic Sans MS", 15))
        labeldescripcion.config(bg="#add6bc")
        labeldescripcion.pack(pady=10)
        ##label ALTURA
        labelAltura=tk.Label(self.ventana, text="ingresa la altura para calcular el area\n", font=("Comic Sans MS", 15))
        labelAltura.config(bg="#f7dece", relief="raised")
        labelAltura.pack(pady=10)
        ##entry altura
        self.altura=tk.Entry(self.ventana)
        self.altura.pack(pady=10)
        #label Base SUPERIOR
        labelBaseS=tk.Label(self.ventana, text="ingresa la base SUPERIOR para calcular el area\n", font=("Comic Sans MS", 15))
        labelBaseS.config(bg="#f7dece", relief="raised")
        labelBaseS.pack(pady=10)
        ##entry base SUPERIOR
        self.baseSuper=tk.Entry(self.ventana)
        self.baseSuper.pack(pady=10)
        #label Base INFERIOR
        labelBaseI=tk.Label(self.ventana, text="ingresa la base INFERIOR para calcular el area\n", font=("Comic Sans MS", 15))
        labelBaseI.config(bg="#f7dece", relief="raised")
        labelBaseI.pack(pady=10)
        ##entry base INFERIOR
        self.baseInfer=tk.Entry(self.ventana)
        self.baseInfer.pack(pady=10)
        
        self.buttonCalculador=tk.Button(self.ventana, text="CALCULAR", command=self.verificarDatos)
        self.buttonCalculador.config(bg="#988864", relief="raised")
        self.buttonCalculador.pack(pady=10)
        return self.ventana
    def controlador(self,Controlador):
        self.controlador=Controlador
    def verificarDatos(self):
        if not self.baseSuper.get() or not self.altura.get() or not self.baseInfer.get():
            messagebox.showerror("Error")
        else: 
            if self.baseSuper.get().isdigit() and self.altura.get().isdigit() and self.baseInfer:
                calcularDatos=[self.baseSuper.get(), self.altura.get(), self.baseInfer.get()]
                self.controlador.procesamientoDatos(calcularDatos)  
            else:
                messagebox.showerror("error, numeros ingresados no validos para ejecutar la operacion\n") 
                
#Utilice isdigit para comprobar si el nuevo valor es un número o si el campo está vacío (permitiendo la eliminación de caracteres).
    def mostrarDatos(self, area):
        self.buttonCalculador.config(state="disabled")
        labelRta=tk.Label(self.ventana, text=f"El area de trapecio es:{area[3]}cm^2")
        labelRta.config(bg="#988864", relief="raised")
        labelRta.pack(pady=10)