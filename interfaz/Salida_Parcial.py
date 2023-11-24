import tkinter as tk
from PIL import Image, ImageTk

def accion_boton():
    texto_ingresado = entrada_texto.get()
    etiqueta_resultado.config(text=f"Texto ingresado: {texto_ingresado}")

root = tk.Tk()
root.title("Interfaz de salida parcial")
root.geometry("800x600") 
espacio_vertical_6 = tk.Label(root, text="", height=5)
espacio_vertical_6.pack()


# Título centrado
titulo = tk.Label(root, text="INGRESO DE VEHICULOS", font=("Arial", 35))
titulo.pack()

espacio_vertical_7 = tk.Label(root, text="", height=5)
espacio_vertical_7.pack()
# Frame para el contenido
frame_contenido = tk.Frame(root)
frame_contenido.pack()


# Texto en el frame
etiqueta_texto = tk.Label(frame_contenido, text="Digite su placa:", font=("Arial",25))
etiqueta_texto.pack()

# Espacio para ingresar texto
entrada_texto = tk.Entry(frame_contenido, font=("Arial", 25),width=30)
entrada_texto.pack()

# Botón en el frame
boton = tk.Button(frame_contenido, text="Continuar",font=("Arial",20), command=accion_boton)
boton.pack()

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(frame_contenido, text="")
etiqueta_resultado.pack()

# Centrar contenido horizontalmente
titulo.pack()
frame_contenido.pack(pady=20)
etiqueta_texto.pack()
entrada_texto.pack()
boton.pack()
etiqueta_resultado.pack()



root.mainloop()