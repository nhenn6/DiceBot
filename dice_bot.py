import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

def roll(sides, quantity):
    total = 0
    while quantity > 0:
        quantity -= 1
        total += random.randint(1, sides)
    return total
    


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    



@bot.command(name='d20')
async def roll_d20(context, args = 1):
    quantity = 1
    try:
        quantity = int(args)
    except:
        await context.send("Quantity must be integer or null")
    quantity = args
    
    total_value = roll(20, quantity)
    
    output = "You rolled: " + str(total_value)
    await context.send(output)
    
@bot.command(name='d10')
async def roll_d10(context, args = 1):

    quantity = 1
    try:
        quantity = int(args)
    except:
        await context.send("Quantity must be integer or null")
    quantity = args
    
    total_value = roll(10, quantity)
    
    output = "You rolled: " + str(total_value)
    await context.send(output)
    
@bot.command(name='d8')
async def roll_d8(context, args = 1):

    quantity = 1
    try:
        quantity = int(args)
    except:
        await context.send("Quantity must be integer or null")
    quantity = args
    
    total_value = roll(8, quantity)
    
    output = "You rolled: " + str(total_value)
    await context.send(output)    
    
@bot.command(name='d6')
async def roll_d6(context, args = 1):

    quantity = 1
    try:
        quantity = int(args)
    except:
        await context.send("Quantity must be integer or null")
    quantity = args
    
    total_value = roll(6, quantity)
    
    output = "You rolled: " + str(total_value)
    await context.send(output)
    
@bot.command(name='d4')
async def roll_d4(context, args = 1):

    quantity = 1
    try:
        quantity = int(args)
    except:
        await context.send("Quantity must be integer or null")
    quantity = args
    
    total_value = roll(4, quantity)
    
    output = "You rolled: " + str(total_value)
    await context.send(output)
    
bot.run(TOKEN)


