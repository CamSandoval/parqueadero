import requests

def obtener_texto():
    url_vehiculos = "http://10.200.10.142:7070/api_parqueadero/vehiculos/xxx242"  # Reemplaza con tu URL de la API
    response = peticion_placa(url_vehiculos)
    
    # Verificar el código de estado de la respuesta
    if response.status_code == 200:
        try:
            # Convertir la respuesta a formato JSON
            data = response.json()

            # Mostrar el resultado completo en una línea
            print("Resultado completo:", data)

            # Mostrar solo el primer atributo del resultado si hay datos
            if data:
                primer_atributo = data[0]
                print("Primer atributo:", primer_atributo)
            else:
                print("No hay datos disponibles")
        except Exception as e:
            print("Error al procesar la respuesta:", e)
    else:
        print('Error en la solicitud. Código de estado:', response.status_code)

def peticion_placa(url):
    response = requests.get(url)
    return response

obtener_texto()
