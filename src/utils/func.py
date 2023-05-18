import requests, json

def getDolarValue(moneda:str, compraOVenta:str) -> int:
    url = "https://api.bluelytics.com.ar/v2/latest"
    response = requests.get(url).json()
    return response[moneda][compraOVenta]

def getConfig() -> dict:
    with open("./src/utils/config.json") as f:
        config = json.load(f)
    return config