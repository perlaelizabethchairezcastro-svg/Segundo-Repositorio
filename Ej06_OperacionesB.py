#CBTIS 89
# Autor: Perla Elizabeth Chairez Castro
# 
#
#
import tkinter as tk

def sumar():
   # TODO: Obtener los valores de las entradas, sumarlos y mostrar el resultado
   pass
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Suma de dos números")
ventana.geometry("350x230")

def sumar():
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      suma = num1 + num2
      resultado.config(text=f"Resultado: {suma}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")

# Crear los cuadros de texto
entrada1 = tk.Entry(ventana)
entrada2 = tk.Entry(ventana)
# Posicionar las entradas en la ventana
entrada1.pack(pady=5)
entrada2.pack(pady=5)

# Crear botón de suma
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=5)

def resta():
   try:
      num3 = float(entrada1.get())
      num4 = float(entrada2.get())
      resta = num3 - num4
      resultado.config(text=f"Resultado: {resta}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")


# Crear botón de suma
boton_restar = tk.Button(ventana, text="Resta", command=resta)
boton_restar.pack(pady=5)

def mult():
   try:
      num5 = float(entrada1.get())
      num6 = float(entrada2.get())
      mult = num5 * num6
      resultado.config(text=f"Resultado: {mult}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")


# Crear botón de suma
boton_multi = tk.Button(ventana, text="Multiplicación", command=mult)
boton_multi.pack(pady=5)

def division():
   try:
      num7 = float(entrada1.get())
      num8 = float(entrada2.get())
      division = num7 / num8
      resultado.config(text=f"Resultado: {division}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")


# Crear botón de suma
boton_divi = tk.Button(ventana, text="Division", command=division)
boton_divi.pack(pady=5)

# Crear etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="Resultado:")
resultado.pack(pady=5)


# Ejecutar la aplicación
ventana.mainloop()