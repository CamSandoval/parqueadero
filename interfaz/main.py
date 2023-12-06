import tkinter as tk
import subprocess 
def accion_boton_1():
    root.destroy()
    subprocess.run(["python3", "./interfaz/interfaz_ingreso_parcial.py"]) 

def accion_boton_2(): 
    root.destroy()
    subprocess.run(["python3", "./interfaz/Salida_Parcial.py"])  
    
def accion_boton_3():
    root.destroy()
    subprocess.run(["python3", "./interfaz/interfaz_control_mensualidades.py"]) 
     
root = tk.Tk()
root.title("PARQUEADERO CENTRAL")


HOST = "localhost"

root.geometry("600x500")  
espacio_vertical_5 = tk.Label(root, text="", height=3)
espacio_vertical_5.pack()
titulo = tk.Label(root, text="PARQUEADERO", font=("Arial", 35))
titulo.pack()

espacio_vertical_2 = tk.Label(root, text="", height=5)
espacio_vertical_2.pack()

subtitulo = tk.Label(root, text="Que desea hacer?", font=("Arial", 25))
subtitulo.pack()

espacio_vertical = tk.Label(root, text="", height=2)
espacio_vertical.pack()

# Frame para contener los botones y centrarlos horizontalmente
frame_botones = tk.Frame(root)
frame_botones.pack()
 
# Tres botones centrados horizontalmente
boton_1 = tk.Button(frame_botones, text="Ingreso parcial", command=accion_boton_1, font=("Arial", 14))
boton_1.pack(side=tk.LEFT, padx=10, pady=10)

boton_2 = tk.Button(frame_botones, text="Salida parcial", command=accion_boton_2, font=("Arial", 14))
boton_2.pack(side=tk.LEFT, padx=10, pady=10)

boton_3 = tk.Button(frame_botones, text="Control de mensualidad", command=accion_boton_3, font=("Arial", 14))
boton_3.pack(side=tk.LEFT, padx=10, pady=10)

# Centrar los botones horizontalmente
frame_botones.pack_configure(anchor=tk.CENTER)

# Iniciar el bucle principal
root.mainloop()

