#CBTIS 89
#Programacion 3B TM
#Autor:Perla Elizabeth Chairez Castro
#Programa que te da a elegir unaopcion y 
#la pone de ese color
import tkinter as tk
from tkinter import ttk

ventana=tk.Tk()
ventana.title("lista desplegable ComboBox")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana,text="Elige una opción: ")
etiqueta.pack(pady=10)

opciones = ["Rojo","Verde","Azul","Amarillo","Morado"]

color_map = {
    "Rojo": "red",
    "Verde": "green",
    "Azul": "blue",
    "Amarillo": "yellow",
    "Morado": "purple",
}

ComboColores=ttk.Combobox(ventana,values=opciones,state="readonly")
ComboColores.pack(pady=5)

def mostrar_seleccion(event):
    seleccion = ComboColores.get()
    color = color_map.get(seleccion, "black")
    etiqueta_resultado.config(text=f"Seleccionaste: {seleccion}", fg=color)

ComboColores.bind("<<ComboboxSelected>>",mostrar_seleccion)

etiqueta_resultado = tk.Label(ventana,text="Aún no has seleccionado nada")
etiqueta_resultado.pack(pady=20)

ventana.mainloop()