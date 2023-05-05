import os, discord
from dotenv import load_dotenv
from discord.ext import commands
def main():
    load_dotenv()
    prefix = "!"
    token = os.getenv("DISCORD_TOKEN")
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=prefix, intents=intents, description="hola, soy el Dolar Bot")

    # commands and events
    @bot.command(name="saludar",help="el bot te saludará")
    async def saludar(ctx):
        await ctx.reply(f"hola {ctx.author}, en que puedo ayudarte")
    
    bot.run(token)

if __name__ == "__main__":
    main()
