import requests, json
from datetime import datetime
from discord import Embed
def getCurrency(moneda:str, compraOVenta:str) -> str:
    url = "https://api.bluelytics.com.ar/v2/latest"
    response = requests.get(url).json()
    return f"${response[moneda][compraOVenta]}"

def filterDicts(dictsToFilter:list):
    filtered_dicts = list()
    for dic in dictsToFilter:
        newDic = {"date", dic["date"]}
        filtered_dicts.append(newDic)
    return filtered_dicts

def getCurrencyByDay(moneda:str, date_str:str):
    date = datetime.strptime("%Y-%m-%d").date()
    evolucion_url = "https://api.bluelytics.com.ar/v2/evolution.json?days=30"
    response = requests.get(evolucion_url).json()
    filtered = filterDicts(response)
    return filtered

def getConfig() -> dict:
    with open("./src/utils/config.json") as f:
        config = json.load(f)
    return config



class CreateResponde:
    def __init__(self, title, post_content):
        self.title = title
        self.content = post_content
        self.response = Embed(title=self.title, description=self.content, colour=int("3377FF", 16))
    @property
    def send(self):
        return self.response
    
    def createFields(self, data: dict) -> None:
        # {"Oficial": getCurrency("oficial", "value_avg"), ...}
        for _, (name, value) in enumerate(data.items()):
            self.response.add_field(name=name, value=value, inline=False)
        self.response.set_footer(text="Fuente: https://www.valordolarblue.com.ar", icon_url="https://i.imgur.com/0FOvHM4.png")
    

