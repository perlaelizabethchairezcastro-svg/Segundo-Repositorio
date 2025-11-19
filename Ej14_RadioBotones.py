#CBTIS 89
#Programacion 3B TM
#Autor:Perla Elizabeth Chairez Castro
#Programa que muestra tres radio botones con diversas
#opciones y al seleccionar cada uno realizar acciones distintas

import tkinter as tk

ventana=tk.Tk()
ventana.title("Calcular Descuentos")
ventana.geometry("500x300")
ventana.resizable(False,False) 

etiqueta_cantidad=tk.Label(ventana,text="Ingresa la cantidad: ")
etiqueta_cantidad.pack()

entrada_cantidad=tk.Entry(ventana, justify="center")
entrada_cantidad.pack()

def ejecutar_radio():
    opcion=Seleccion.get()

    if opcion==1:
        cantidad=float(entrada_cantidad.get())
        descuento=cantidad*0.05
        etiqueta_resultado.config(text=f"Hola estimado cliente usted obtuvo un descuento del 5%,el cual equivale a: ${descuento:.2f}")

    elif opcion==2:
        cantidad=float(entrada_cantidad.get())
        descuento=cantidad*0.10
        etiqueta_resultado.config(text=f"Hola estimado cliente usted obtuvo un descuento del 10%,el cual equivale a: ${descuento:.2f}")

    elif opcion==3:
        cantidad=float(entrada_cantidad.get())
        descuento=cantidad*0.15
        etiqueta_resultado.config(text=f"Hola estimado cliente usted obtuvo un descuento del 15%,el cual equivale a: ${descuento:.2f}")

Seleccion = tk.IntVar()

radioB1=tk.Radiobutton(ventana, text="Descuento del 5%", variable=Seleccion, value=1,command=ejecutar_radio)
radioB2=tk.Radiobutton(ventana, text="Descuento del 10%", variable=Seleccion, value=2,command=ejecutar_radio)
radioB3=tk.Radiobutton(ventana, text="Descuento del 15%", variable=Seleccion, value=3,command=ejecutar_radio)

radioB1.pack(pady=10)
radioB2.pack(pady=10)
radioB3.pack(pady=10)

etiqueta_resultado=tk.Label(ventana,text="Aun no has seleccionado nada")
etiqueta_resultado.pack(pady=20)

ventana.mainloop()