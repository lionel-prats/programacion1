# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

NOMBRE = "" # Nombre del alumno

"""
#Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar 
    en la bolsa de valores.:

A) Para ello deberás programar el botón  para poder cargar 10 operaciones de compra 
    con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    Son 10 datos

B) Al presionar el botón mostrar 
    
    Informe 1 - Se deberán listar todos los datos de los usuarios y su posición en la lista (por terminal) 

# IMPORTANTE:
Del punto C solo deberá realizar SOLAMENTE 2 informes. 
(PRESUPONER QUE CADA CLIENTE INGRESADO ES UN CLIENTE DISTINTO, NINGUNO SE REPITE, 
no es necesario validar que no haya nombres repetidos)

Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 2 - Tome el último número de su DNI Personal (Ej 4) 
        y realice ese informe (Ej, Realizar informe 4)

    Informe 3 - Tome el último número de su DNI Personal (Ej 4), 
        y restarle al número 9 (Ej 9-4 = 5). En caso de que su DNI 
        finalice con el número 0, deberá realizar el informe 9.

    Realizar los informes correspondientes a los números obtenidos. 
        EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Tipo de instrumento que menos se operó en total.
    #! 1) - Tipo de instrumento que más se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion de la persona que menos BONOS compro
    #! 6) - Nombre y posicion del usuario que invirtio menos dinero
    #! 7) - Nombre y posicion del usuario que mas cantidad de instrumentos compró
    #! 8) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 9) - Promedio de cantidad de instrumentos  MEP vendidos en total
"""

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Bolsa de valores de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Bolsa de valores {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar cartas", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_informe_5 = customtkinter.CTkButton(master=self, text="Informe 5", command=self.btn_mostrar_informe_5)
        self.btn_informe_5.grid(row=7, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_informe_6 = customtkinter.CTkButton(master=self, text="Informe 6", command=self.btn_mostrar_informe_6)
        self.btn_informe_6.grid(row=8, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_informe_7 = customtkinter.CTkButton(master=self, text="Informe 7", command=self.btn_mostrar_informe_7)
        self.btn_informe_7.grid(row=9, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_informe_8 = customtkinter.CTkButton(master=self, text="Informe 8", command=self.btn_mostrar_informe_8)
        self.btn_informe_8.grid(row=10, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_informe_9 = customtkinter.CTkButton(master=self, text="Informe 9", command=self.btn_mostrar_informe_9)
        self.btn_informe_9.grid(row=11, pady=10, columnspan=2, sticky="nsew")
    
        #PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS

        # * Nombre
        # * Monto en pesos de la operación (no menor a $10000)
        # * Tipo de instrumento(CEDEAR, BONOS, MEP) 
        # * Cantidad de instrumentos  (no menos de cero) 

        self.array_nombres = ["Lionel", "Alex", "Luis", "Rodrigo", "Mariano", "Valeria", "Belén", "Rafael", "Tomás", "Carolina"]
        self.array_montos = [25000, 17500, 32400, 21000, 16800, 50000, 14900, 12000, 11000, 15600]
        self.array_instrumentos = ["BONOS", "BONOS", "MEP", "CEDEAR", "MEP", "MEP", "MEP", "CEDEAR", "BONOS", "CEDEAR"]
        self.array_cantidad_instrumentos = [120, 150, 50, 250, 200, 90, 275, 20, 40, 210]
        
    # Informe 1 - Se deberán listar todos los datos de los usuarios y su posición en la lista (por terminal)
    def btn_mostrar_todos_on_click(self):
        print("Nombre | monto | instrumento | cantidad")
        for i in range(len(self.array_nombres)):
            print(f"{self.array_nombres[i]} | {self.array_montos[i]} | {self.array_instrumentos[i]} | {self.array_cantidad_instrumentos[i]}")

    #! 0) - Tipo de instrumento que menos se operó en total.
    def btn_mostrar_informe_0(self):
        total_usuarios = len(self.array_nombres)
        for i in range(total_usuarios):
            if(True):
                pass
        print(f"")

    # 0) - Tipo de instrumento que menos se operó en total.
    def btn_mostrar_informe_1(self):
        
        total_usuarios = len(self.array_nombres)
        total_bonos_operados = 0
        total_cedear_operados = 0
        total_mep_operados = 0
        instrumento_menos_operado = ""

        for i in range(total_usuarios):
            if(self.array_instrumentos[i] == "BONOS"):
                total_bonos_operados += self.array_cantidad_instrumentos[i]
            elif(self.array_instrumentos[i] == "CEDEAR"):
                total_cedear_operados += self.array_cantidad_instrumentos[i]
            else:
                total_mep_operados += self.array_cantidad_instrumentos[i]

        mensaje = "Instrumento menos operado: "
        if(total_bonos_operados < total_cedear_operados):
            if(total_bonos_operados < total_mep_operados):
                mensaje += "BONOS"
            elif(total_bonos_operados > total_mep_operados):
                mensaje += "MEP"
            else:
                mensaje += "BONOS y MEP"
        elif(total_bonos_operados > total_cedear_operados):
            if(total_cedear_operados < total_mep_operados):
                mensaje += "CEDEAR"
            elif(total_cedear_operados > total_mep_operados):
                mensaje += "MEP"
            else:
                mensaje += "CEDEAR y MEP"
        else:
            if(total_bonos_operados < total_mep_operados):
                mensaje += "BONOS y CEDEAR"
            elif(total_bonos_operados > total_mep_operados):
                mensaje += "MEP"
            else:
                mensaje += "BONOS, CEDEAR y MEP"
        
        print(mensaje)

    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    def btn_mostrar_informe_2(self):
        total_usuarios = len(self.array_nombres)
        contador_mep_50_200 = 0

        for i in range(total_usuarios):
            if(self.array_instrumentos[i] == "MEP" and (self.array_cantidad_instrumentos[i] >= 50 and self.array_cantidad_instrumentos[i] <= 200)):
                contador_mep_50_200 += 1
        
        print(f"Cantidad de usuarios que compraron entre 50 y 200 MEP: {contador_mep_50_200}")

    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    def btn_mostrar_informe_3(self):
        total_usuarios = len(self.array_nombres)
        acumulador_no_cedear = 0
        for i in range(total_usuarios):
            if(self.array_instrumentos[i] != "CEDEAR"):
                acumulador_no_cedear += 1
        print(f"Cantidad de usuarios que no compraron CEDEAR: {acumulador_no_cedear}")

    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    def btn_cargar_datos_on_click(self):
        total_usuarios = len(self.array_nombres)
        for i in range(total_usuarios):
            if(True):
                pass
        print(f"")

    #! 5) - Nombre y posicion de la persona que menos BONOS compro
    def btn_mostrar_informe_5(self):
        total_usuarios = len(self.array_nombres)
        for i in range(total_usuarios):
            if(True):
                pass
        print(f"")

    #! 6) - Nombre y posicion del usuario que invirtio menos dinero
    def btn_mostrar_informe_6(self):
        total_usuarios = len(self.array_nombres)
        primera_iteracion = True
        menor_monto_ivertido = 0
        nombre_menor_monto_invertido = ""
        posicion_menor_monto_invertido = ""
        for i in range(total_usuarios):
            if(primera_iteracion):
                menor_monto_ivertido = self.array_montos[i]
                nombre_menor_monto_invertido = self.array_nombres[i]
                posicion_menor_monto_invertido = i
                primera_iteracion = False
            elif(self.array_montos[i] < menor_monto_ivertido):
                menor_monto_ivertido = self.array_montos[i]
                nombre_menor_monto_invertido = self.array_nombres[i]
                posicion_menor_monto_invertido = i
                
        print(f"Posición y nombre del usuario con menor inversión: {posicion_menor_monto_invertido}) {nombre_menor_monto_invertido}")
    
    #! 7) - Nombre y posicion del usuario que mas cantidad de instrumentos compró
    def btn_mostrar_informe_7(self):
        total_usuarios = len(self.array_nombres)
        primera_iteracion = True
        for i in range(total_usuarios):
            if(primera_iteracion):
                pass
            elif(True):
                pass
        print(f"")
    
    #! 8) - Promedio de dinero en CEDEAR  ingresado en total.  
    def btn_mostrar_informe_8(self):
        
        total_usuarios = len(self.array_nombres)

        total_dinero = 0
        total_dindero_cedear = 0

        for i in range(total_usuarios):
            total_dinero += self.array_montos[i]
            if(self.array_instrumentos[i] == "CEDEAR"):
                total_dindero_cedear += self.array_montos[i]
            
        
        print(f"Total dinero facturado: ${total_dinero}")
        print(f"Total dinero facturado por CEDEARs: ${total_dindero_cedear}")
        print(f"El dinero facturado por CEDEARs representan un {(total_dindero_cedear / total_dinero * 100):.2f}% del total de dinero facturado")
    
    #! 9) - Promedio de cantidad de instrumentos  MEP vendidos en total
    def btn_mostrar_informe_9(self):

        total_usuarios = len(self.array_nombres)

        total_instrumentos = 0
        total_instrumentos_mep = 0

        for i in range(total_usuarios):
            total_instrumentos += self.array_cantidad_instrumentos[i]
            if(self.array_instrumentos[i] == "MEP"):
                total_instrumentos_mep += self.array_cantidad_instrumentos[i]
            
        print(f"Total instrumentos vendidos: {total_instrumentos}")
        print(f"Total MEP vendidos: {total_instrumentos_mep}")
        print(f"Los MEP representan un {(total_instrumentos_mep / total_instrumentos * 100):.2f}% del total de instrumentos vendidos")

















if __name__ == "__main__":
    app = App()
    app.mainloop()
