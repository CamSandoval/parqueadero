import tkinter as tk
from tkinter import messagebox
import main
import requests
import json
import re

def registrar_vehiculo(placa,carroceria,mensualidad):
    mensualidadData = False
    if mensualidad == "SI":
        mensualidadData= True
        
    data = {
    "placa": placa,
    "tipo": carroceria,
    "mensualidad":mensualidadData
    }
    json_data = json.dumps(data)

    # Cabecera (headers) indicando el tipo de contenido
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        # Realizar la solicitud GET a la API
        url_registro=f"http://{main.HOST}:7070/api_parqueadero/vehiculos/crear"
        respuesta = requests.post(url_registro,data=json_data, headers=headers)

        # Verificar si la solicitud fue exitosa (código 200)
        if respuesta.status_code == 201:
            # Mostrar el resultado en formato JSON en la consola
            mensaje = "Registro exitoso"
            # Agregar espacios en blanco al principio para centrar visualmente el texto
            mensaje_centralizado = "\n\n\n" + " " * 15 + mensaje
            messagebox.showinfo("Mensaje", mensaje_centralizado)
            root.destroy()
        

        else:
            mensaje = "Registro fallido, por favor rectifique los datos"
            # Agregar espacios en blanco al principio para centrar visualmente el texto
            mensaje_centralizado = "\n\n\n" + " " * 15 + mensaje
            messagebox.showinfo("Mensaje", mensaje_centralizado)
    except requests.RequestException as e:
        # Capturar errores de solicitud y mostrar el mensaje de error
        print(f"Error de solicitud: {e}")

def recoger_datos():
    placa=entrada1.get()
    carroceria=seleccion_var.get()
    mensualidad=seleccion_var2.get()
    if validar_string(placa):
        registrar_vehiculo(placa,carroceria,mensualidad)
    else:
        mensaje = "la placa ingresada no es valida"
        # Agregar espacios en blanco al principio para centrar visualmente el texto
        mensaje_centralizado = "\n\n\n" + " " * 15 + mensaje
        messagebox.showinfo("Mensaje", mensaje_centralizado)
    
def validar_string(input_str):
    # Define la expresión regular para un string alfanumérico de 6 caracteres
    patron = re.compile(r'^[a-zA-Z0-9]{6}$')

    # Intenta hacer coincidir el string con el patrón
    if patron.match(input_str):
        return True
    else:
        return False

root = tk.Tk()
root.title("Registro de mensualidades")
root.geometry("600x500") 
espacio_vertical_b= tk.Label(root, text="", height=5)
espacio_vertical_b.pack()

# Título centrado
titulo = tk.Label(root, text="Registro de mensualidades", font=("Arial", 20))
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

texto3 = tk.Label(frame_contenido, text="Mensualidad",font=("Arial", 20), padx=10)
texto3.grid(row=0, column=2)

# Tres espacios de textos centrados horizontalmente un al lado del otro
entrada1 = tk.Entry(frame_contenido,font=("Arial", 13))
entrada1.grid(row=3, column=0)

opciones = ["MOTO", "SEDAN","CAMIONETA","CAMION","BUSETA","BOLQUETA"]
seleccion_var = tk.StringVar()
seleccion_var.set(opciones[0])  # Selecciona la primera opción por defecto
seleccion = tk.OptionMenu(frame_contenido,seleccion_var, *opciones)
seleccion.grid(row=3,column=1)


opcionesMensualidad = ["SI", "NO"]
seleccion_var2 = tk.StringVar()
seleccion_var2.set(opcionesMensualidad[0])  # Selecciona la primera opción por defecto
seleccion2 = tk.OptionMenu(frame_contenido,seleccion_var2, *opcionesMensualidad)
seleccion2.grid(row=3,column=2)

espacio_vertical_d= tk.Label(root, text="", height=5)
espacio_vertical_d.pack()
# Botón centrado
boton = tk.Button(root, text="Continuar",font=("Arial", 20), command=recoger_datos)
boton.pack()


# Centrar contenido horizontalmente
titulo.pack()
frame_contenido.pack()
boton.pack()

# Iniciar el bucle principal
root.mainloop()
