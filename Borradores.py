import tkinter as tk

def on_button_click():
    label.config(text="¡Hola, " + entry.get() + "!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Interfaz Gráfica")

# Crear y agregar un widget de etiqueta (label)
label = tk.Label(ventana, text="Introduce tu nombre:")
label.pack(pady=10)

# Crear y agregar un widget de entrada de texto (entry)
entry = tk.Entry(ventana)
entry.pack(pady=10)

# Crear y agregar un widget de botón (button)
button = tk.Button(ventana, text="Saludar", command=on_button_click)
button.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()