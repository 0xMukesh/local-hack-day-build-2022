import os
import discord
import json

from discord.ext import commands
from PIL import Image
from io import BytesIO

from recognize import Recognize

with open('config.json', 'r') as f:
    config = json.load(f)
TOKEN = config['token']

client = commands.Bot(command_prefix="-")


@client.event
async def on_ready():
    print("🦈 I'm ready!")


@client.command()
async def recognize(ctx):
    image_url = ctx.message.attachments[0].url
    image_format_jpg = image_url[-3:]
    image_format_jpeg = image_url[-4:]
    if image_format_jpg.lower() == 'jpg' or image_format_jpeg.lower() == 'jpeg':
        try:
            brain = Recognize()
            results = brain.analyze_image(image_url)[0]
            message = discord.Embed(
                title="Let's have a look..")
            for statistic in results:
                name = statistic[1]
                value = f'{round(statistic[2] * 100, 2)} %'
                message.add_field(name=name, value=value, inline=False)
            message.set_image(url=image_url)
            message.colour = 0x00ff00
            await ctx.message.channel.send(embed=message)
        except:
            error = discord.Embed(
                title="Ops.. Something went wrong", description="I'm sorry, something went wrong. Please, try again.")
            error.colour = 0xff0000
            await ctx.message.channel.send(embed=error)
            raise discord.DiscordException
    else:
        invalid_format = discord.Embed(
            title="Invalid format", description="I'm sorry, this format is not supported. Please, try again with a .jpg or .jpeg!")
        invalid_format.colour = 0xff0000
        await ctx.message.channel.send(embed=invalid_format)

client.run(TOKEN)
