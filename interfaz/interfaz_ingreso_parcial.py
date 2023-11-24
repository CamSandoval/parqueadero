import tkinter as tk
from tkinter import messagebox
import main
import requests
import json
import subprocess

def accion_boton():
    texto_ingresado = entrada_texto.get()
    etiqueta_resultado.config(text=f"Texto ingresado: {texto_ingresado}")

def bahias_disponibles(carroceria,id):
    try:
        # Realizar la solicitud GET a la API
        url_registro=f"http://{main.HOST}:7070/api_parqueadero/bahias/disponibles/{carroceria}"
        respuesta = requests.get(url_registro)

        # Verificar si la solicitud fue exitosa (código 200)
        if respuesta.status_code == 200:
            data=respuesta.json()
            print(data)
            #print(type(data))
            ids_string = ''
            if(len(data)>0):
                for elemento in data:
                    ids_string += str(elemento['id']) + ','

                if ids_string.endswith(','):
                    ids_string = ids_string[:-1]

                frame_contenido_dinamico = tk.Frame(root)
                frame_contenido_dinamico.pack()
                widgets = frame_contenido_dinamico.winfo_children()
                for widget in widgets:
                    # Destruir cada widget
                    widget.destroy()

                espacio_vertical_7 = tk.Label(frame_contenido_dinamico, text="", height=5)
                espacio_vertical_7.pack()

                etiqueta_texto = tk.Label(frame_contenido_dinamico, text="Las siguientes bahias estan disponibles: ", font=("Arial",25))
                etiqueta_texto.pack()

                etiqueta_de_bahia = tk.Label(frame_contenido_dinamico, text=ids_string, font=("Arial",25))
                etiqueta_de_bahia.pack()
                # Espacio para ingresar texto
                entrada_texto_bah = tk.Entry(frame_contenido_dinamico, font=("Arial", 25),width=30)
                entrada_texto_bah.pack()

                def llamar():
                    texto= entrada_texto_bah.get()
                    peticion_revision_de_registro(texto,id)

                    

                # Botón en el frame
                boton = tk.Button(frame_contenido, text="Registrar Ingreso",font=("Arial",20), 
                                  command=llamar)
                boton.pack()

            else:
                mensaje = "No hay bahías disponibles para el tipo de carrocería de su vehículo."
                # Agregar espacios en blanco al principio para centrar visualmente el texto
                mensaje_centralizado = "\n\n\n" + " " * 15 + mensaje
                messagebox.showinfo("Mensaje", mensaje_centralizado)

        

        else:
            # Mostrar el mensaje de error si la solicitud no fue exitosa
            print(f"La solicitud no fue exitosa. Código de estado: {respuesta.status_code}")
    except requests.RequestException as e:
        # Capturar errores de solicitud y mostrar el mensaje de error
        print(f"Error de solicitud: {e}")

def obtener_bahia(data):
    return data.get()

def peticion_revision_de_registro(id_bahia,id_vehiculo):
    data = {
    "id_vehiculo": id_vehiculo,
    "id_bahia": id_bahia
    }
    print("id_bah",data["id_bahia"])
    print("id_veh",data["id_vehiculo"])
    # Convertir los datos a formato JSON
    json_data = json.dumps(data)

    # Cabecera (headers) indicando el tipo de contenido
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        # Realizar la solicitud GET a la API
        url_registro=f"http://{main.HOST}:7070/api_parqueadero/registros/crear"
        respuesta = requests.post(url_registro,data=json_data, headers=headers)

        # Verificar si la solicitud fue exitosa (código 200)
        if respuesta.status_code == 201:
            # Mostrar el resultado en formato JSON en la consola
            print("Resultado de la solicitud:")
            print(respuesta.json())
        

        else:
            # Mostrar el mensaje de error si la solicitud no fue exitosa
            print(f"La solicitud no fue exitosa. Código de estado: {respuesta.status_code}")
    except requests.RequestException as e:
        # Capturar errores de solicitud y mostrar el mensaje de error
        print(f"Error de solicitud: {e}")


def peticion_placa(url):
    try:
        # Realizar la solicitud GET a la API
        respuesta = requests.get(url)

        # Verificar si la solicitud fue exitosa (código 200)xx
        if respuesta.status_code == 200:
            # Mostrar el resultado en formato JSON en la consola
            print("Resultado de la solicitud:")
            data=respuesta.json()
            id=data['id']
            carroceria=data['tipo']
            print(respuesta.json())
            #print(type(diccionario))
            bahias_disponibles(carroceria,id)

        else:
            # Mostrar el mensaje de error si la solicitud no fue exitosa
            print(f"La solicitud no fue exitosa. Código de estado: {respuesta.status_code}")
    except requests.RequestException as e:
        # Capturar errores de solicitud y mostrar el mensaje de error
        print(f"Error de solicitud: {e}")


def obtener_texto():
    texto_ingresado = entrada_texto.get()
    url_vehiculos=f"http://{main.HOST}:7070/api_parqueadero/vehiculos/{texto_ingresado}"
    peticion_placa(url_vehiculos)

root = tk.Tk()
root.title("Interfaz con Entrada de Texto")
root.geometry("10000x1000") 
espacio_vertical_3 = tk.Label(root, text="", height=1)
espacio_vertical_3.pack()

# Título centrado
titulo = tk.Label(root, text="INGRESO DE VEHICULOS", font=("Arial", 35))
titulo.pack()


# Frame para el contenido
frame_contenido = tk.Frame(root)
frame_contenido.pack()

# Texto en el frame
etiqueta_texto = tk.Label(frame_contenido, text="Digite su placa:", font=("Arial",25))
etiqueta_texto.pack()

# Espacio para ingresar texto
entrada_texto = tk.Entry(frame_contenido,font=("Arial", 25), width=30)
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

# Iniciar el bucle principal
root.mainloop()
