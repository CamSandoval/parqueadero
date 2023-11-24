import tkinter as tk

def accion_boton():
    etiqueta_resultado.config(text="Botón presionado")

root = tk.Tk()
root.title("Interfaz con Textos, Entradas y Botón")
root.geometry("600x500") 
espacio_vertical_b= tk.Label(root, text="", height=5)
espacio_vertical_b.pack()

# Título centrado
titulo = tk.Label(root, text="Registro de Mensualidad", font=("Arial", 20))
titulo.pack()
espacio_vertical_c= tk.Label(root, text="", height=5)
espacio_vertical_c.pack()
# Frame para el contenido
frame_contenido = tk.Frame(root)
frame_contenido.pack()

# Tres textos centrados horizontalmente uno al lado del otro
texto1 = tk.Label(frame_contenido, text="Placa",font=("Arial", 20), padx=10)
texto1.grid(row=0, column=0)

texto2 = tk.Label(frame_contenido, text="Carroceria", font=("Arial", 20),padx=10)
texto2.grid(row=0, column=1)

texto3 = tk.Label(frame_contenido, text="Telefono",font=("Arial", 20), padx=10)
texto3.grid(row=0, column=2)

# Tres espacios de textos centrados horizontalmente un al lado del otro
entrada1 = tk.Entry(frame_contenido,font=("Arial", 13))
entrada1.grid(row=3, column=0)

entrada2 = tk.Entry(frame_contenido,font=("Arial", 13))
entrada2.grid(row=3, column=1)

entrada3 = tk.Entry(frame_contenido,font=("Arial", 13))
entrada3.grid(row=3, column=2)

espacio_vertical_d= tk.Label(root, text="", height=5)
espacio_vertical_d.pack()
# Botón centrado
boton = tk.Button(root, text="Continuar",font=("Arial", 20), command=accion_boton)
boton.pack()

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(root, text="")
etiqueta_resultado.pack()

# Centrar contenido horizontalmente
titulo.pack()
frame_contenido.pack()
boton.pack()
etiqueta_resultado.pack()

# Iniciar el bucle principal
root.mainloop()
