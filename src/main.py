import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Context, Bot
from datetime import datetime
from utils.func import *
def main():
    
    config = getConfig()
    
    prefix = config["prefix"]
    token = config["token"]
    
    intents = discord.Intents.all()
    
    bot = Bot(command_prefix=prefix, intents=intents, description="hola, soy el Dolar Bot")

    @bot.event
    async def on_ready():
        print("The bot is ready")

    @bot.event
    async def on_command_error(ctx: Context, error):
        if isinstance(error, commands.CommandNotFound):
            response = CreateResponde(title="Comando no encontrado", post_content="Ingrese `!help` para información de los comandos")
            await ctx.reply(embed = response.send)

        elif isinstance(error, commands.MissingRequiredArgument):
            response = CreateResponde(title="Ese parámetro no existe!", post_content="Tienes que ingresar un parametro válido")
            data = {"**Opciones**": "- `!dolar hoy`\n- `!dolar reciente`\n- `!euro hoy`\n- `!euro reciente`"}
            response.createFields(data)
            
            await ctx.reply(embed = response.send)

    @bot.command(name="saludo")
    async def saludo(ctx, nombre=None):
        if nombre:
            await ctx.send(f"Hola, {nombre}!")
        else:
            await ctx.send("¡Hola!")

    ALLOWED_PARAMS = ["hoy", "dia"]
    @bot.command(name="dolar", help="Este comando proporcionará la cotizacion del dólar oficial y el dólar blue")
    async def dolar(ctx: Context, param, date=None):
        async with ctx.typing():

            if param not in ALLOWED_PARAMS:
                await ctx.reply("Ese parámetro no existe")
            elif param == "hoy":
                date = datetime.now().strftime("%d/%m/%y %H:%M:%S")
                respuesta = CreateResponde(title="Cotizacion dólar", post_content=f"Ultima actualización: {date}")
                data = {"Oficial": getCurrency("oficial", "value_avg"), "Blue": getCurrency("blue", "value_avg")}
                respuesta.createFields(data)
                await ctx.reply(embed = respuesta.send)
            elif param == "dia" and date:
                filtered = getCurrencyByDay(date)
                print(filtered)
                await ctx.reply("Esta es la cotización de los últimos 30 días")
            
                   
    @bot.command(name="euro", help="Este comando proporcionará la cotizacion del euro oficial y el euro blue")
    async def euro(ctx: Context, param):
        if param not in ALLOWED_PARAMS:
            await ctx.reply("Ese parámetro no existe")
        elif param == "hoy":
            date = datetime.now().strftime("%d/%m/%y %H:%M:%S")
            respuesta = CreateResponde(title=f"Cotizacion euro", post_content=f"Ultima actualización: {date}")
            data = {"Oficial": getCurrency("oficial_euro", "value_avg"), "Blue": getCurrency("blue_euro", "value_avg")}
            respuesta.createFields(data)
            
            await ctx.reply(embed = respuesta.send)
        elif param == "dia" and date:
            await ctx.reply("Esta es la cotizacion del euro en los ultimos 30 días")

    bot.run(token)

if __name__ == "__main__":
    main()
