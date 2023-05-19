import os, discord
from discord.ext.commands import Context, Bot
from datetime import datetime
from utils.func import *
def main():
    
    config = getConfig()
    
    prefix = config["prefix"]
    token = config["token"]
    
    intents = discord.Intents.all()
    bot = Bot(command_prefix=prefix, intents=intents, description="hola, soy el Dolar Bot")


    @bot.command(name="saludar", help="el bot te saludará")
    async def saludar(ctx: Context):
        await ctx.reply(f"hola {ctx.author}, en que puedo ayudarte")

    @bot.command(name="dólar", help="")
    async def dolar(ctx: Context):
        date = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        respuesta = CreateResponde(title=f"Cotizacion dolar", post_content=f"Ultima actualización: {date}")
        respuesta.configureEmbed()

        await ctx.reply(embed = respuesta.send)
        
    @bot.command(name="euro", help="")
    async def euro(ctx: Context):
        date = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        respuesta = CreateResponde(title=f"Cotizacion euro", post_content=f"Ultima actualización: {date}")
        respuesta.configureEmbed()

        await ctx.reply(embed = respuesta.send)
    bot.run(token)

if __name__ == "__main__":
    main()
