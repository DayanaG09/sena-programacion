import tkinter as tk
from tkinter import messagebox

class VistaPrisma:
    def __init__(self, interfazPrincipal):
        self.altura=None
        self.longitud=None
        self.ancho=None
        self.ventana= interfazPrincipal
       
        
    def obtenerDatos(self):
        self.ventana.title("--------------CALCULADOR DEL VOLUMEN DE UN PRISMA--------------- ")
        self.ventana.geometry("700x800")
        self.ventana.config(bg= "#44749d", height=500, width=500 ) 
        labeldescripcion=tk.Label(self.ventana, text="ESTE PROGRAMA ESTA DISEÑADO PARA CALCULAR EL VOLUMEN DE UN PRISMA", font=("Comic Sans MS", 15))
        labeldescripcion.config(bg="#44749d")
        labeldescripcion.pack(pady=10)
        labeldescripcion=tk.Label(self.ventana, text="A continuación ingresa los datos que te solicitan\n ", font=("Comic Sans MS", 15))
        labeldescripcion.config(bg="#44749d")
        labeldescripcion.pack(pady=10)
        ##label ALTURA
        labelAltura=tk.Label(self.ventana, text="ingresa la altura para calcular el Volumen del prisma \n", font=("Comic Sans MS", 15))
        labelAltura.config(bg="#ffffff", relief="raised")
        labelAltura.pack(pady=10)
        ##entry altura
        self.altura=tk.Entry(self.ventana)
        self.altura.pack(pady=10)
        #label longitud
        labelLongitud=tk.Label(self.ventana, text="ingresa el largo  para calcular el Volumen del prisma\n", font=("Comic Sans MS", 15))
        labelLongitud.config(bg="#ffffff", relief="raised")
        labelLongitud.pack(pady=10)
        ##entry longitud
        self.longitud=tk.Entry(self.ventana)
        self.longitud.pack(pady=10)
        #label ancho
        labelAncho=tk.Label(self.ventana, text="ingresa el ancho para calcular el area prisma \n", font=("Comic Sans MS", 15))
        labelAncho.config(bg="#ffffff", relief="raised")
        labelAncho.pack(pady=10)
        ##entry ancho
        self.ancho=tk.Entry(self.ventana)
        self.ancho.pack(pady=10)
        
        self.buttonCalculador=tk.Button(self.ventana, text="CALCULAR", command=self.verificarDatos)
        self.buttonCalculador.config(bg="#bdb8ad", relief="raised")
        self.buttonCalculador.pack(pady=10)
        return self.ventana
    def controlador(self,Controlador):
        self.controlador=Controlador
    def verificarDatos(self):
        if not self.longitud.get() or not self.altura.get() or not self.ancho.get():
            messagebox.showerror("Error")
        else: 
            if self.longitud.get().isdigit() and self.altura.get().isdigit() and self.ancho.get():
                calcularDatos=[self.longitud.get(), self.altura.get(), self.ancho.get()]
                self.controlador.procesamientoDatos(calcularDatos)  
            else:
                messagebox.showerror("error, numeros ingresados no validos para ejecutar la operacion\n") 
                
#Utilice isdigit para comprobar si el nuevo valor es un número o si el campo está vacío (permitiendo la eliminación de caracteres).
    def mostrarDatos(self, volumen):
        self.buttonCalculador.config(state="disabled")
        labelRta=tk.Label(self.ventana, text=f"El Volumen del prisma  es:{volumen[3]}cm^3")
        labelRta.config(bg="#bdb8ad", relief="raised")
        labelRta.pack(pady=10)