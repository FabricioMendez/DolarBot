import discord
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
        command_string = ""
        for command in bot.commands:
            command_string += f"- `{bot.command_prefix}{command.name}`: {command.help}\n"
       
        if isinstance(error, commands.CommandNotFound):
            response = CreateResponse(title="Comando no encontrado", post_content="")
            data = {"Opciones": command_string}
            response.createFields(data)
            await ctx.reply(embed = response.send)

        elif isinstance(error, commands.MissingRequiredArgument):
            response = CreateResponse(title="Ese parámetro no existe!", post_content="Tienes que ingresar un parametro válido")
            prefix = bot.command_prefix
            data = {"**Opciones**": f"- `{prefix}dolar hoy`\n- `{prefix}dolar dia 'fecha' 'oficial o blue'`\n\tej: `{prefix}dolar dia 2023-05-29 oficial`"}

            response.createFields(data)
            
            await ctx.reply(embed = response.send)

    @bot.command(name="saludo",help="Este comando te saludará")
    async def saludo(ctx, nombre=None):
        if nombre:
            await ctx.send(f"Hola, {nombre}!")
        else:
            await ctx.send("¡Hola!")

    ALLOWED_PARAMS = ["hoy", "dia"]
    @bot.command(name="dolar", help="Este comando proporcionará la cotizacion del dólar oficial y el dólar blue")
    async def dolar(ctx: Context, param, date_str=None, moneda=None):
        async with ctx.typing():

            if param not in ALLOWED_PARAMS:
                response = CreateResponse(title="Error!", post_content="Ese comando no existe", color=int("fd0204", 16))
                await ctx.reply(embed = response.send)
            elif param == "hoy":
                date = datetime.now().strftime("%d/%m/%y %H:%M:%S")
                respuesta = CreateResponse(title="Cotizacion dólar", post_content=f"Ultima actualización: {date}")
                data = {"Oficial": getCurrency("oficial", "value_avg"), "Blue": getCurrency("blue", "value_avg")}
                respuesta.createFields(data)
                await ctx.reply(embed = respuesta.send)
            elif param == "dia" and date_str and moneda:
                moneda_seleccionada = getCurrencyByDay(moneda, date_str)
                date = datetime.strptime(date_str, "%Y-%m-%d")
                formatted_date = date.strftime("%d de %B de %Y")
                response = CreateResponse(title=f"Cotización del dólar {moneda}", post_content=formatted_date)
                data = {"Valor Venta": moneda_seleccionada["value_sell"], "Valor Compra": moneda_seleccionada["value_buy"]}
                response.createFields(data)
                await ctx.reply(embed  = response.send)
            
                   
    @bot.command(name="euro", help="Este comando proporcionará la cotizacion del euro oficial y el euro blue")
    async def euro(ctx: Context):
        async with ctx.typing():
            date = datetime.now().strftime("%d/%m/%y %H:%M:%S")
            respuesta = CreateResponse(title=f"Cotizacion euro", post_content=f"Ultima actualización: {date}")
            data = {"Oficial": getCurrency("oficial_euro", "value_avg"), "Blue": getCurrency("blue_euro", "value_avg")}
            respuesta.createFields(data)
            await ctx.reply(embed = respuesta.send)
            
    @bot.command(name="ban", help="Comando para banear un usuario del servidor")
    @commands.has_permissions(ban_members=True)
    async def ban(ctx:Context, member: discord.Member):
        await member.ban()
        await ctx.send(f"{member.mention} ha sido baneado por {ctx.author.mention}")


    bot.help_command = CustomHelpCommand(bot)
    bot.run(token)

if __name__ == "__main__":
    main()
