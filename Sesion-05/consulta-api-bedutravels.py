import json
import requests


url = "http://127.0.0.1:8000/api/users/"
r = requests.get(url)
print("Código de estado de la respuesta:", r.status_code)
if r.status_code == 200:
    # Tenemos una respuesta del API
    print("-"*50)
    print("Encabezados:")
    print("-"*50)
    print(r.headers)

    print("-"*50)
    print("Datos en formato texto plano:")
    print("-"*50)
    print(r.text)

    print("-"*50)
    print("Tipo de dato python:")
    print("-"*50)
    datos_python = r.json()
    print( type(datos_python) )

    print("-"*50)
    print("Obteniendo los datos del último usuario:")
    print("-"*50)
    ultimo_usuario = datos_python[-1]
    print( ultimo_usuario )
    print("-"*50)
    print( json.dumps(ultimo_usuario, indent=4) )


