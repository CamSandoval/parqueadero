import tkinter as tk
import subprocess 
def accion_boton_1():
     subprocess.run([
"python3", "./interfaz/retiroMensualidades.py"])  

def accion_boton_2():
     subprocess.run([
"python3", "./interfaz/registro_mensualidad.py"])      

root = tk.Tk()
root.title("Interfaz con Botones")
root.geometry("600x500") 
espacio_vertical_9= tk.Label(root, text="", height=5)
espacio_vertical_9.pack()

# Título centrado
titulo = tk.Label(root, text="MENSUALIDADES", font=("Arial", 20))
titulo.pack()
espacio_vertical_a= tk.Label(root, text="", height=5)
espacio_vertical_a.pack()
# Frame para el contenido
frame_contenido = tk.Frame(root)
frame_contenido.pack()

# Texto en el frame
etiqueta_texto = tk.Label(frame_contenido, text="Que desea hacer:",font=("Arial", 25))
etiqueta_texto.pack()

# Frame para los botones
frame_botones = tk.Frame(frame_contenido)
frame_botones.pack()

# Dos botones alineados horizontalmente
boton_1 = tk.Button(frame_botones, text="Retirar ",font=("Arial", 20), command=accion_boton_1)
boton_1.pack(side=tk.LEFT, padx=5)

boton_2 = tk.Button(frame_botones, text="Registrar",font=("Arial", 20), command=accion_boton_2)
boton_2.pack(side=tk.LEFT, padx=5)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(frame_contenido, text="")
etiqueta_resultado.pack()

# Centrar contenido horizontalmente
titulo.pack()
frame_contenido.pack(pady=20)
etiqueta_texto.pack()
frame_botones.pack()
etiqueta_resultado.pack()

# Iniciar el bucle principal
root.mainloop()


