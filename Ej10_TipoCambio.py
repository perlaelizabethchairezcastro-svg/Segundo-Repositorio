#CBTIS 89
#Programacion 3B TM
#Autor:Perla Elizabeth Chairez Castro
#Programa que alcula en dolares, euros
#libras y yanes de una cantidad

import tkinter as tk
from tkinter import messagebox

def calcular_euros():
    try:
        cantidad=float(entrada_cantidad.get())
        euros=cantidad *0.47
        etiqueta_resultado.config(text=f"El euro equivale a $0.47: {euros:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una cantidad valida")

def calcular_dolares():
    try:
        cantidad=float(entrada_cantidad.get())
        dolar=cantidad *0.054
        etiqueta_resultado.config(text=f"El dolar equivale a $0.054: {dolar:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una cantidad valida")

def calcular_libras():
    try:
        cantidad=float(entrada_cantidad.get())
        libras=cantidad *0.041
        etiqueta_resultado.config(text=f"El dolar equivale a $0.041: {libras:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una cantidad valida")

def calcular_yanes():
    try:
        cantidad=float(entrada_cantidad.get())
        yanes=cantidad *8.21
        etiqueta_resultado.config(text=f"El yanes equivale a $8.21: {yanes:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una cantidad valida")

ventana = tk.Tk()
ventana.title("DIVISAS")
ventana.geometry("380x300")
ventana.resizable(False, False)

# Etiqueta y caja de texto para ingresar la cantidad

#cREAMOS UNA ETIQUETA QUE INDICA QUE DEBE ESCRIBIR EL USUARIO
etiqueta_cantidad = tk.Label(ventana, text="Cantidad:")
etiqueta_cantidad.pack(pady=10)

#Caja de texto donde se escribe la cantidad
entrada_cantidad = tk.Entry(ventana, width=20)
entrada_cantidad.pack()

#Botones de accion

# Botones para calcular IVA
boton_dolar = tk.Button(ventana, text="Calcular Dolar", command=calcular_dolares, bg="#9370DB", fg="white")
boton_dolar.pack(pady=5)

# Botones para calcular descuento 
boton_euro = tk.Button(ventana, text="Calcular Euro", command=calcular_euros, bg="#FF69B4", fg="white")
boton_euro.pack(pady=5)

# Botones para calcular total
boton_libra = tk.Button(ventana, text="Calcular Libra", command=calcular_libras, bg="#DDA0DD", fg="white")
boton_libra.pack(pady=5)

boton_yanes = tk.Button(ventana, text="Calcular Yanes", command=calcular_yanes, bg="#FFC5FF", fg="white")
boton_yanes.pack(pady=5)

# Etiqueta para mostrar resultados
#Aqui se mostrara el resultado despues de presionar un boton
etiqueta_resultado = tk.Label(ventana, text="", font=("Times New Roman", 12, "bold"))
etiqueta_resultado.pack(pady=10)

#inicio del programa 
# Ejecutar el bucle principal de la ventana
ventana.mainloop()