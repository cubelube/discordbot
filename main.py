import asyncio
import os
import random

import discord
from discord.ext import commands

from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
TOKEN = os.environ['TOKEN']

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def echo(ctx, arg: str):
  await ctx.send(arg)


@bot.command()
async def add(ctx, add1: int, add2: int):
  await ctx.send(add1 + add2)


@bot.command()
async def subtract(ctx, sub1: int, sub2: int):
  await ctx.send(sub1 - sub2)


@bot.command()
async def multiply(ctx, mul1: int, mul2: int):
  await ctx.send(mul1 * mul2)


@bot.command()
async def divide(ctx, div1: int, div2: int):
  await ctx.send(div1 / div2)


@bot.command()
async def roll(ctx, dice: int):
  diceroll = random.randint(1, dice)
  await ctx.send(diceroll)


@bot.command()
async def dm(message):
  await message.author.send('👋')


@bot.command()
async def code(ctx):
  await ctx.send(
      "https://replit.com/@Supernova283/LinedPalatableInitialization#main.py")

@bot.command()
async def guess(ctx, guess1: int):
  randomnumber = random.randint(1, 2)
  if guess1 == randomnumber:
    await ctx.send("Your guess was correct!")
  else:
    await ctx.send("Your guess was incorrect.")

@bot.command()
async def username(ctx):    
  await ctx.send(Client.fetch_user())

@bot.command()
async def dectobin(ctx, dec: int):
  binnum = bin(dec)
  await ctx.send(binnum)

@bot.command()
async def bintodec(ctx, bin):
  decnum = int(bin, 2)
  await ctx.send(decnum)

@bot.command()
async def coinflip(ctx):
  result = random.randint(1, 2)
  await ctx.send(result)

keep_alive()
bot.run(TOKEN)
