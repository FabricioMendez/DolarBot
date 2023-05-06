# 

import requests

response = requests.get('https://api.bluelytics.com.ar/v2/latest?callback=cotizacion')
print(response.status_code)  # 200 si la petición fue exitosa
print(response.json())  # contenido de la respuesta en formato JSON
