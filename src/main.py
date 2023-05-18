import os, discord
from discord.ext.commands import Context, Bot
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
    
    
    @bot.command(name="greet", help="this command will greet")
    async def greet(ctx: Context, name):
        await ctx.send(f"hola {name}")

    @bot.command(name="dolar", help="el bot te va a dar informacion sobre el dolar")
    async def dolar(ctx: Context, moneda, compraOventa):
        await ctx.send(f"El valor del dolar esta a {getDolarValue(moneda, compraOventa)}")
    

    @bot.command(name="euro", help="el bot te va a dar informacion sobre el euro")
    async def euro(ctx: Context, moneda, compraOventa):
        await ctx.send(f"El valor del euro esta a {getDolarValue(moneda, compraOventa)}")
    

    bot.run(token)

if __name__ == "__main__":
    main()
