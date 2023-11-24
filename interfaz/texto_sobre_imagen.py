import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz con imagen de fondo")

# Cargar la imagen de fondo
ruta_imagen = "logo2.png"  # Reemplaza con la ruta de tu imagen
imagen = Image.open(ruta_imagen)
imagen = imagen.resize((800, 600))  # Ajustar tamaño según la ventana
imagen_de_fondo = ImageTk.PhotoImage(imagen)

# Crear un widget de lienzo para la imagen de fondo
lienzo = tk.Canvas(root, width=800, height=600)
lienzo.pack(fill="both", expand=True)
lienzo.create_image(0, 0, image=imagen_de_fondo, anchor="nw")


# Agregar un título centrado
titulo = tk.Label(root, text="Bienvenido!!!", font=("Arial", 24), bg="white")
titulo.place(relx=0.5, rely=0.3, anchor="center")

root.mainloop()
