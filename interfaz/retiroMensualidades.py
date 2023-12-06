import tkinter as tk
from tkinter import messagebox
import requests
import subprocess
import main
import json

def cambiarMensualidad(placa):
    try:
        # Realizar la solicitud GET a la API
        url_registro=f"http://{main.HOST}:7070/api_parqueadero/vehiculos/mensualidad/retirar/{placa}"
        respuesta = requests.put(url_registro)

        # Verificar si la solicitud fue exitosa (código 200)
        if respuesta.status_code == 200:
            data=respuesta.json()
            # Mostrar el resultado en formato JSON en la consola
            mensaje = f"Mensualidad Retirada a el vehiculo de placa: {data['placa']}"
            # Agregar espacios en blanco al principio para centrar visualmente el texto
            mensaje_centralizado = "\n\n\n" + " " * 15 + mensaje
            messagebox.showinfo("Mensaje", mensaje_centralizado)
            root.destroy()
            subprocess.run(["python3", "./interfaz/main.py"])  
        

        else:
            mensaje = "Retiro Fallido"
            # Agregar espacios en blanco al principio para centrar visualmente el texto
            mensaje_centralizado = "\n\n\n" + " " * 15 + mensaje
            messagebox.showinfo("Mensaje", mensaje_centralizado)
    except requests.RequestException as e:
        # Capturar errores de solicitud y mostrar el mensaje de error
        print(f"Error de solicitud: {e}")

def peticion_placa(placa):
    url_vehiculos=f"http://{main.HOST}:7070/api_parqueadero/vehiculos/{placa}"
    try:
        # Realizar la solicitud GET a la API
        respuesta = requests.get(url_vehiculos)

        # Verificar si la solicitud fue exitosa (código 200)xx
        if respuesta.status_code == 200:
            # Mostrar el resultado en formato JSON en la consola
            print("Resultado de la solicitud:")
            data=respuesta.json()
            id=data['id']
            carroceria=data['tipo']
            placa=data['placa']
            mensualidad=data['mensualidad']
            print(respuesta.json())
            #print(type(diccionario))
            if mensualidad:
                cambiarMensualidad(placa)
            else:
                mensaje = "El vehiculo no cuenta con mensualidad activa "
                # Agregar espacios en blanco al principio para centrar visualmente el texto
                mensaje_centralizado = "\n\n\n" + " " * 15 + mensaje
                messagebox.showinfo("Mensaje", mensaje_centralizado)
                return

        else:
            mensaje = "Su vehiculo no se encuentra registrado en la base de datos"
            # Agregar espacios en blanco al principio para centrar visualmente el texto
            mensaje_centralizado = "\n\n\n" + " " * 15 + mensaje
            messagebox.showinfo("Mensaje", mensaje_centralizado)
            
    except requests.RequestException as e:
        # Capturar errores de solicitud y mostrar el mensaje de error
        print(f"Error de solicitud: {e}")

def registro_Activo(id):
    url_vehiculos=f"http://{main.HOST}:7070/api_parqueadero/registros/{id}"
    try:
        # Realizar la solicitud GET a la API
        respuesta = requests.get(url_vehiculos)

        # Verificar si la solicitud fue exitosa (código 200)xx
        if respuesta.status_code == 200:
            data=respuesta.json()
            registro=data["registrActivo"]
            return registro

            
    except requests.RequestException as e:
        # Capturar errores de solicitud y mostrar el mensaje de error
        print(f"Error de solicitud: {e}")

    
def obtener_texto():
    placa = entrada_texto.get()
    peticion_placa(placa)

root = tk.Tk()
root.title("Interfaz de retiro de mensualidades")
root.geometry("800x600") 
espacio_vertical_6 = tk.Label(root, text="", height=5)
espacio_vertical_6.pack()


# Título centrado
titulo = tk.Label(root, text="RETIRO DE MENSUALIDADES", font=("Arial", 35))
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
boton = tk.Button(frame_contenido, text="Continuar",font=("Arial",20), command=obtener_texto)
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