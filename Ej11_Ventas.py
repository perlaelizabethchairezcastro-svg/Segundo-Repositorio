#CBTIS 89
#Programacion 3B TM
#Autor:Perla Elizabeth Chairez Castro
#Programa que calcula el numero de ventas

import tkinter as tk
from tkinter import messagebox

def calcular_subtotal():
    try:
        subtotal=int(entrada_cantidad.get())
        cantidad=int(entrada_cantidad.get())
        precio=int(entrada_precio.get())
        subtotal=cantidad*precio 
        etiqueta_resultado.config(text=f"El subtotal es:${subtotal:.2f}")

    except ValueError:
        messagebox.showerror("Error","Por favor ingresa una cantidad valida")

def calcular_iva():
    try:
        cantidad=int(entrada_cantidad.get())
        precio=int(entrada_precio.get())
        subtotal=cantidad*precio 
        iva=subtotal*0.16 
        etiqueta_resultado.config(text=f"El subtotal es:{precio:.2f}")

    except ValueError:
        messagebox.showerror("Error","Por favor ingresa una cantidad valida")

def calcular_total():
    try:
        cantidad=int(entrada_cantidad.get())
        precio=int(entrada_precio.get())
        subtotal=cantidad*precio 
        iva=subtotal*0.16 
        total=subtotal+iva 
        etiqueta_resultado.config(text=f"El total es:${total:.2f}")

    except ValueError:
        messagebox.showerror("Error","Por favor ingresa una cantidad valida")

ventana = tk.Tk()
ventana.title("DIVISAS")
ventana.geometry("350x300")
ventana.resizable(False, False)

# Etiqueta y caja de texto para ingresar la cantidad

#cREAMOS UNA ETIQUETA QUE INDICA QUE DEBE ESCRIBIR EL USUARIO
etiqueta_cantidad = tk.Label(ventana, text="Cantidad:")
etiqueta_cantidad.pack(pady=10)
entrada_cantidad = tk.Entry(ventana, width=20)
entrada_cantidad.pack()

etiqueta_cantidad = tk.Label(ventana, text="Precio por el articulo:")
etiqueta_cantidad.pack(pady=10)
entrada_precio = tk.Entry(ventana, width=20)
entrada_precio.pack()

#Botones de accion

# Botones para calcular IVA
boton_subtotal = tk.Button(ventana, text="Subtotal", command=calcular_subtotal, bg="#9370DB", fg="white")
boton_subtotal.pack(pady=5)

# Botones para calcular descuento 
boton_iva = tk.Button(ventana, text="IVA", command=calcular_iva, bg="#FF69B4", fg="white")
boton_iva.pack(pady=5)

# Botones para calcular total
boton_total = tk.Button(ventana, text="Total", command=calcular_total, bg="#DDA0DD", fg="white")
boton_total.pack(pady=5)

# Etiqueta para mostrar resultados
#Aqui se mostrara el resultado despues de presionar un boton
etiqueta_resultado = tk.Label(ventana, text="", font=("Times New Roman", 12, "bold"))
etiqueta_resultado.pack(pady=10)

#inicio del programa 
# Ejecutar el bucle principal de la ventana
ventana.mainloop()