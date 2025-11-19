#Autor: Perla Elizabeth Chairez Castro
#3B Programación TM
#Crea un programa con dos botones. 
#Cada botón abrirá una ventana. 
#La primera ventana contendrá etiquetas con tu nombre 
# y apellidos y la segunda ventana tendrá el mensaje,
#  «Programado con Python».


import tkinter as tk
from tkinter import Toplevel

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")
ventana_principal.geometry("300x200")

# Función para abrir una ventana hija
def abrir_ventana_hija():
    ventana_hija = Toplevel(ventana_principal)
    ventana_hija.title("Ventana Hija")
    ventana_hija.geometry("250x150")
    
    etiqueta = tk.Label(ventana_hija, text="Perla Castro", font=("Arial", 12))
    etiqueta.pack(pady=10)
    
    boton_cerrar = tk.Button(ventana_hija, text="Cerrar", command=ventana_hija.destroy)
    boton_cerrar.pack(pady=10)

def abrir_ventana_hija2():
    ventana_hija2 = Toplevel(ventana_principal)
    ventana_hija2.title("Ventana Hija")
    ventana_hija2.geometry("250x150")
    
    etiqueta2 = tk.Label(ventana_hija2, text="Programado con Python", font=("Arial", 12))
    etiqueta2.pack(pady=10)
    
    boton_cerrar2 = tk.Button(ventana_hija2, text="Cerrar", command=ventana_hija2.destroy)
    boton_cerrar2.pack(pady=10)

# Botón en la ventana principal para abrir la ventana hija
boton_abrir = tk.Button(ventana_principal, text="Abrir Ventana Hija", command=abrir_ventana_hija)
boton_abrir.pack(pady=20)

boton_abrir = tk.Button(ventana_principal, text="Abrir Ventana Hija", command=abrir_ventana_hija2)
boton_abrir.pack(pady=20)

# Iniciar el loop principal
ventana_principal.mainloop()