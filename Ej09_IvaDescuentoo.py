#CBTIS 89
#Programacion 3B TM
#Autor:Perla Elizabeth Chairez Castro
#Programa que muestra una ventana, en la cual
#esta una caja de texto, y tres botones para
#realizar diversos calculos.

import tkinter as tk
from tkinter import messagebox

#FUNCIONES PRINCIPALES

# Función para calcular el IVA (Impuesto al Valor Agregado 16%)
def calcular_iva():
    try:
        #Obtenemos el valor que el usuario escribio en la caja de texto
        cantidad = float(entrada_cantidad.get()) #Convertimos el texto a numero decimal
        
        #Calculamos el 16%
        iva = cantidad * 0.16
        
        #Mostramos el resultado en la etiqueta de resultados 
        etiqueta_resultado.config(text=f"IVA (16%): ${iva:.2f}")
    
    #Si el usuario no ingresa el numero, mostramos un mensaje de error
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una cantidad válida.")

# Función para calcular el 10% de descuento
def calcular_descuento():
    try:
        #Obtenemos el valor ingresado por el usuario
        cantidad = float(entrada_cantidad.get())

        #Calculamos el 10% de descuento
        descuento = cantidad * 0.10

        #Mostramos el resultado en la etiqueta
        etiqueta_resultado.config(text=f"Descuento (10%): ${descuento:.2f}")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una cantidad válida.")

# Función para calcular el total a pagar (considerando IVA y descuento)
def calcular_total():
    try:
        cantidad = float(entrada_cantidad.get())

        #Calculamos IVA y descuento
        iva = cantidad * 0.16
        descuento = cantidad * 0.10

        #Total = cantidad original + IVA - descuento
        total = cantidad + iva - descuento

        #Mostramos el total en la pantalla
        etiqueta_resultado.config(text=f"Total a pagar: ${total:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una cantidad válida.")

#INTERFAZ GRAFICA DE LA VENTANA PRINCIPAL

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de IVA y Descuento")
ventana.geometry("350x200")
ventana.resizable(False, False)

# Etiqueta y caja de texto para ingresar la cantidad

#cREAMOS UNA ETIQUETA QUE INDICA QUE DEBE ESCRIBIR EL USUARIO
etiqueta_cantidad = tk.Label(ventana, text="Ingresa la cantidad:")
etiqueta_cantidad.pack(pady=10)

#Caja de texto donde se escribe la cantidad
entrada_cantidad = tk.Entry(ventana, width=20)
entrada_cantidad.pack()

#Botones de accion

# Botones para calcular IVA
boton_iva = tk.Button(ventana, text="Calcular IVA (16%)", command=calcular_iva, bg="#9370DB", fg="white")
boton_iva.pack(pady=5)

# Botones para calcular descuento 
boton_descuento = tk.Button(ventana, text="Calcular Descuento (10%)", command=calcular_descuento, bg="#FF69B4", fg="white")
boton_descuento.pack(pady=5)

# Botones para calcular total
boton_total = tk.Button(ventana, text="Calcular Total a Pagar", command=calcular_total, bg="#DDA0DD", fg="white")
boton_total.pack(pady=5)

# Etiqueta para mostrar resultados
#Aqui se mostrara el resultado despues de presionar un boton
etiqueta_resultado = tk.Label(ventana, text="", font=("Times New Roman", 12, "bold"))
etiqueta_resultado.pack(pady=10)

#inicio del programa 
# Ejecutar el bucle principal de la ventana
ventana.mainloop()