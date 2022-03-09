import discord
from discord.ext import commands,tasks
import youtube_dl
import random
from random import choice
import os
import music
from dotenv import load_dotenv
import sfx

load_dotenv()

TOKEN = os.getenv("TOKEN")

cogs = [music]
coggs = [sfx]
status = '?help to use me dipshit'
client = commands.Bot(command_prefix='?')

class general(commands.Cog):
    def __init__(self,client):
        self.client = client
    @client.event
    async def on_ready():
        #change_status.start()
        print('Music Bot is online!')
        await client.change_presence(activity=discord.Game(status))

    for i in range(len(cogs)):
        cogs[i].setup(client)
        coggs[i].setup(client)

    @client.command(name='ping',help='Returns latency')
    async def ping(ctx):
        await ctx.send(f'Latency: {round(client.latency * 1000)} ms')

client.run(TOKEN)