# Suponiendo que respuesta contiene una lista de JSONs, por ejemplo:
respuesta = [
    {"id": 1, "nombre": "Ejemplo 1"},
    {"id": 2, "nombre": "Ejemplo 2"},
    {"id": 3, "nombre": "Ejemplo 3"}
]

# Inicializamos un string vacío para almacenar los valores de 'id'
ids_string = ''

# Recorremos la lista de JSONs y concatenamos los valores de 'id' en el string
for elemento in respuesta:
    ids_string += str(elemento['id']) + ','  # Agregamos el 'id' seguido de una coma

# Eliminamos la última coma del string resultante si es necesario
if ids_string.endswith(','):
    ids_string = ids_string[:-1]

print(ids_string)  # Imprimimos el string resultante
