#CBTIS 89
#Autor:Perla Elizabeth Chairez Castro
#Programacion 3B TM
#Programa que 

import tkinter as tk
from tkinter import ttk

#Crear una ventana principales
ventana=tk.Tk()
ventana.title("Carrearas")
ventana.geometry("300x200")

#Etiqueta de instruccion 
etiqueta=tk.Label(ventana, text="Eige una opcion:")
etiqueta.pack(pady=10)

#Crear la lista desplegable (ComboBox)
opciones=["ARH","Arquitectatura","Comercio electronico","Comercio Internacional y Aduanas"
"Construccion","Contabilidad","Mecatronca","Programacion"]
ComboColores=ttk.Combobox(ventana, values=opciones,state="readonly")
ComboColores.pack(pady=5)

#Funcion que se ejecuta al seleccionar un elemento
def mostrar_seleccion(event):
    seleccion=ComboColores.get() #Obtiene el vaor seleccionado
    etiqueta_resultado.config(text=f"Seleccionaste: {seleccion}")

#Asociar evento al seleccionar un elemento
ComboColores.bind("<<ComboboxSelected>>", mostrar_seleccion)

#Etiqueta para mostrr el resultado
etiqueta_resultado=tk.Label(ventana, text="Aun no has seleccionado nada")
etiqueta_resultado.pack(pady=20)

#Iniciar bucle principales
ventana.mainloop()