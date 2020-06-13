# bot.py
import random
from random import randrange
import os

import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

import emotes as em
import matplot as mp
import scrapper as sc
import os


TOKEN = os.getenv('BOT_TOKEN')

client = discord.Client()
client = commands.Bot(command_prefix='!')




@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')
    game = discord.Game(name="with Graphs")
    await client.change_presence(status=discord.Status.idle, activity=game)


@client.command()
async def kick(ctx,a:discord.Member):
    if str(client.user.id) in ctx.message.content:
        return

    if '626276117266956310' in ctx.message.content:
        return

    kick=em.kick()
    await ctx.send(f"You desreve to get kicked <@!{a.id}> "+kick)


@client.command()
async def smile(ctx): 
    smile= em.smile()
    await ctx.send(smile)



@client.command()
async def plot(ctx,y:str):
    if y=="help":
        await ctx.send(mp.plot.__doc__)
        return
    mp.plot(y)
    with open('An bot\\plot.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@client.command()
async def plot3D(ctx,y:str):
    mp.plot3D(y)
    with open('An bot\\plot3D.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@client.command()
async def TOW(ctx):
    latest=sc.check()
    await ctx.send("> Latest Chapter of [ Throne of World ] is: "+ str(latest))


@client.command()
async def insult(ctx, usr: discord.Member):
    if str(client.user.id) in ctx.message.content:
        return
    if '626276117266956310' in ctx.message.content:
        return
    insult=sc.insult()
    await ctx.send(f'<@!{usr.id}> ' +insult)


@client.command()
async def advice(ctx):
    adv= sc.advice()
    await ctx.send(adv)


@client.command()
async def define(ctx,word : str):
    mean=sc.define(word)
    await ctx.send(mean)

@client.command()
async def rate(ctx, currency: str ):
    r=sc.rate(currency)
    await ctx.send(r)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("Command not available! :sweat:")
    await ctx.send(error)



client.run(TOKEN)
