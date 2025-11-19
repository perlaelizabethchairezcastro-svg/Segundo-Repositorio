#CBTIS 89
#Autor:Perla Elizabeth Chairez Castro
#Programa que muestra una ventana con
#una etiquetla y un boton
 
#Importamos la libreria Tkinter y le damos un alias "tk" 
import tkinter as tk

#crea la ventana principal 
ventana=tk.Tk() #Instancia principal de la aplicacion 

#Configurar el titulo de la ventana
ventana.title("Ventana de saludo")

#Definir el tamaño de la ventana (ancho x alto)
ventana.geometry("400x300")

#Agregr un texto (etiqueta)
etiqueta=tk.Label(ventana, text="Hola, buenos dias", font=("Arial",16))
etiqueta.pack(pady=10) #"Pack" coloca el elemento  en la ventna y el "pady" da especificaciones 

#Agregar un boton 
def saludar():
    etiqueta.config(text="Que tal, como va tu dia?") 

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack(pady=10)

#Ejecutar el bucle principal de la aplicacion 
ventana.mainloop()


