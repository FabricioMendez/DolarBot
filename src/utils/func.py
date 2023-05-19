import requests, json
from discord import Embed
def getCurrency(moneda:str, compraOVenta:str) -> int:
    url = "https://api.bluelytics.com.ar/v2/latest"
    response = requests.get(url).json()
    return response[moneda][compraOVenta]

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
    
    def configureEmbed(self):
        if "dólar" in self.title:
            self.response.add_field(name="Oficial", value=getCurrency("oficial", "value_avg"), inline=False)
            self.response.add_field(name="Blue", value=getCurrency("blue", "value_avg"), inline=False)
        if "euro" in self.title:
            self.response.add_field(name="Oficial", value=getCurrency("oficial_euro", "value_avg"), inline=False)
            self.response.add_field(name="Blue", value=getCurrency("blue_euro", "value_avg"), inline=False)
