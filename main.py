import discord
import requests

client = discord.Client()

async def onReady():
    print(f'Logged in as {client.user}')

