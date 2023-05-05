import discord
import os

bot = discord.Client()

@bot.event
async def on_ready():
    guild_count = 0