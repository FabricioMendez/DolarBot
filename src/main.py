import os, discord
from discord.ext import commands
from utils import getDolarValue, getConfig
def main():
    
    config = getConfig()
    prefix = config["prefix"]
    application_id = config["application_id"]
    token = config["token"]
    
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=prefix, intents=intents, description="hola, soy el Dolar Bot")
    
     
    @bot.command(name="saludar", help="el bot te saludará")
    async def saludar(ctx):
        await ctx.reply(f"hola {ctx.author}, en que puedo ayudarte")
    
    @bot.command(name="dolarhoy", help="cotizacion de dolar ...")
    async def dolarhoy(ctx):
        await ctx.reply(f"el dolar esta a 478")

    bot.run(token)

if __name__ == "__main__":
    main()
