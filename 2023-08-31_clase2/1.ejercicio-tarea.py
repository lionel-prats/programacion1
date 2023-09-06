# GDB del ejercicio -> https://www.onlinegdb.com/rxyUWX64N

""" 
ENUNCIADO: 
Ejercicio Integrador 01

La división de higiene está trabajando en un control de stock para productos sanitarios. 
Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
El tipo (validar "barbijo", "jabón" o "alcohol")
El precio: (validar entre 100 y 300)
La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
La marca y el Fabricante.
  
Se debe informar lo siguiente:
Del más caro de los barbijos, la cantidad de unidades y el fabricante.
Del ítem con más unidades, el fabricante.
Cuántas unidades de jabones hay en total.

Ejemplo de mensaje de consola:

El mas caro de los barbijos tiene una cantidad de: 100 unidades es fabricado por: L1
El item con mas unidades es: L1 y es: 100
La cantidad de jabones es: 320
Gracias por usar el programa 
"""
import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

NOMBRE = "Lionel Prats"

class App(customtkinter.CTk):
    
    def _init_(self):
        super()._init_()
        
        self.title(f"UTN FRA - Bolsa de valores de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Bolsa de valores de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Productos", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=6, pady=10, columnspan=2, sticky="nsew")

        # self.lista_tipo = ["jabón","alcohol","alcohol","barbijo","barbijo"]
        # self.lista_precio = [250, 180, 160, 250, 270]
        # self.lista_cantidad = [520, 180, 700, 640, 80]
        # self.lista_marca = ["Procenex", "Ayudín", "Cif", "Magistral", "Mr. Músculo"]
        # self.lista_fabricante = ["Johnson", "Unilever", "Arcor", "Danone", "Mondelez"]
        self.lista_tipo = []
        self.lista_precio = []
        self.lista_cantidad = []
        self.lista_marca = []
        self.lista_fabricante = []
    
    def btn_cargar_datos_on_click(self):
        for i in range(5):
            # El tipo (validar "barbijo", "jabón" o "alcohol")
            tipo = None
            while tipo != "alcohol" and tipo != "barbijo" and tipo != "jabón":  
                tipo = prompt(title = "Tipo", prompt = "Ingrese el tipo de producto")
            self.lista_tipo = tipo
            
            # El precio: (validar entre 100 y 300)
            precio = None
            while precio == None or not precio.isdigit() or not (int(precio) >= 100 and int(precio) <= 300):  
                precio = prompt(title = "Precio", prompt = "Ingrese el precio del producto")
            self.lista_precio = precio
            
            # La cantidad de unidades (no puede ser 0 ni negativo y no debe superar las 1000 unidades)
            cantidad = None
            while cantidad == None or not cantidad.isdigit() or not (int(cantidad) >= 1 and int(cantidad) <= 1000):  
                cantidad = prompt(title = "Cantidad", prompt = "Ingrese el cantidad de unidades del producto")
            self.lista_cantidad = cantidad
            
            # La marca
            marca = None
            while marca == None or marca == "" or not marca.isalpha():  
                marca = prompt(title = "Marca", prompt = "Ingrese la marca del producto")
            self.lista_marca = marca
            
            # el Fabricante
            fabricante = None
            while fabricante == None or fabricante == "" or not fabricante.isalpha():  
                fabricante = prompt(title = "Fabricante", prompt = "Ingrese la fabricante del producto")
            self.lista_fabricante = fabricante

    def btn_mostrar_todos_on_click(self):

        # Del ítem con más unidades, el fabricante.
        item_mayor_cantidad = 0
        tipo_item_mayor_cantidad = ""
        fabricante_item_mayor_cantidad = ""

        # Del más caro de los barbijos, la cantidad de unidades y el fabricante.
        mayor_precio_barbijo = 0
        cantidad_barbijo_mayor_precio = 0
        fabricante_barbijo_mayor_precio = 0

        # Cuántas unidades de jabones hay en total.
        total_jabon = 0

        for i in range(5):
            tipo = self.lista_tipo[i]
            precio = self.lista_precio[i]
            cantidad = self.lista_cantidad[i]
            fabricante = self.lista_fabricante[i]
            
            # Del ítem con más unidades, el fabricante.
            if cantidad > item_mayor_cantidad:
                item_mayor_cantidad = cantidad
                tipo_item_mayor_cantidad = tipo
                fabricante_item_mayor_cantidad = fabricante

            # Del más caro de los barbijos, la cantidad de unidades y el fabricante.
            if tipo == "barbijo": 
                if precio > mayor_precio_barbijo: 
                    mayor_precio_barbijo = precio
                    cantidad_barbijo_mayor_precio = cantidad
                    fabricante_barbijo_mayor_precio = fabricante

            # Cuántas unidades de jabones hay en total.
            if tipo == "jabón":
                total_jabon += cantidad 
                        
        print("\n----------\n")
        # Del más caro de los barbijos, la cantidad de unidades y el fabricante.
        print(f"El mas caro de los barbijos tiene una cantidad de {cantidad_barbijo_mayor_precio} unidades y es fabricado por {fabricante_barbijo_mayor_precio}")
        # Del ítem con más unidades, el fabricante.
        print(f"El item con mas unidades ({item_mayor_cantidad}) es {tipo_item_mayor_cantidad} y es fabricado por {fabricante_item_mayor_cantidad}")
        # Cuántas unidades de jabones hay en total.
        print(f"La cantidad de jabones es {total_jabon}")
        print("Gracias por usar el programa")

if _name_ == "_main_":
    app = App()
    app.mainloop()