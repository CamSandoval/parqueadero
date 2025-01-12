import tkinter as tk
from tkinter import messagebox
import requests
import subprocess
import main
import json

def dar_salida(id,placa,tipo,mensualidad):
    data = {
    "id":id,
    "placa": placa,
    "tipo": tipo,
    "mensualidad":mensualidad
    }
    json_data = json.dumps(data)
    print(data)

    # Cabecera (headers) indicando el tipo de contenido
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        # Realizar la solicitud GET a la API
        url_registro=f"http://{main.HOST}:7070/api_parqueadero/registros/salidas"
        respuesta = requests.put(url_registro,data=json_data, headers=headers)

        # Verificar si la solicitud fue exitosa (código 200)
        if respuesta.status_code == 200:
            data=respuesta.json()
            # Mostrar el resultado en formato JSON en la consola
            mensaje = f"salida exitosa, hora de entrada: {data['hora_ingreso']}, hora de salida: {data['hora_salida']}, con un total a pagar de: {data['pago']} pesos"
            # Agregar espacios en blanco al principio para centrar visualmente el texto
            mensaje_centralizado = "\n\n\n" + " " * 15 + mensaje
            messagebox.showinfo("Mensaje", mensaje_centralizado)
            root.destroy()
            subprocess.run(["python3", "./interfaz/main.py"])  
        

        else:
            mensaje = "Salida fallida, por favor rectifique los datos"
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
            if registro_Activo(id):
                dar_salida(id,placa,carroceria,mensualidad)
            else:
                mensaje = "El vehiculo no se encuentra dentro del parqueadero "
                # Agregar espacios en blanco al principio para centrar visualmente el texto
                mensaje_centralizado = "\n\n\n" + " " * 15 + mensaje
                messagebox.showinfo("Mensaje", mensaje_centralizado)
                return

        else:
            mensaje = "Su vehiculo no esta registrado en el parqueadero"
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
root.title("Interfaz de salida parcial")
root.geometry("800x600") 
espacio_vertical_6 = tk.Label(root, text="", height=5)
espacio_vertical_6.pack()


# Título centrado
titulo = tk.Label(root, text="SALIDA DE VEHICULOS", font=("Arial", 35))
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