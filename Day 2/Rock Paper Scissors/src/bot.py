import discord
from discord import player
from discord import colour
from discord.ext import commands
from discord.ext.commands.errors import BadArgument, CommandNotFound, MissingRequiredArgument
import random
import json

with open('config.json', 'r') as f:
    config = json.load(f)
TOKEN = config['token']

client = commands.Bot(command_prefix="-", help_command=None)

choices = ["rock", "paper", "scissors"]


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="-help"))
    print("We Are Ready Now")


@client.command(name="help")
async def help(ctx):
    embed = discord.Embed(
        name="Commands"
    )
    embed.add_field(
        name="Rock Paper Scissors",
        value="**rps [your move]`**, **`p [your move]`**, **`game [your move]`**, **`game [your move]`**",
        inline=False
    )
    await ctx.send(embed=embed)


@client.command(name="rps", aliases=["p", "play", "game"], pass_context=True)
async def rps(ctx, move):
    computer = random.choice(choices)

    embed = discord.Embed(
        name="Moves",
        colour=discord.Color.dark_grey()
    )

    if move == "":
        await ctx.send("Please provide a valid argument <:pandaBruh:925953615938605086>")
    else:
        res = ''
        if move.lower() not in ["rock", "paper", "scissors"]:
            await ctx.reply("The argument should be either `rock` or `paper` or `scissors` <:pandaBruh:925953615938605086>")
        else:
            if move.lower() == "rock":
                if computer == "scissors":
                    res = (f"{ctx.author.mention} Wins!")
                elif computer == "paper":
                    res = ("Bot Wins!")
            elif move.lower() == "paper":
                if computer == "rock":
                    res = (f"{ctx.author.mention} Wins!")
                elif computer == "scissors":
                    res = ("Bot Wins!")
            elif move.lower() == "scissors":
                if computer == "paper":
                    res = (f"{ctx.author.mention} Wins!")
                elif computer == "rock":
                    res = ("Bot Wins!")
            else:
                errorEmbed = discord.Embed(
                    description="Something Went Wrong!",
                    color=discord.Color.red()
                )
                await ctx.reply(embed=errorEmbed)

            embed.add_field(
                name="Players Moves",
                value=f"""
                    <@{ctx.message.author.id}> choice - **{move}**,
                    Bot's choice -  **{computer}**
                    Result - **{res}** <:worryCool:925957597599760394>
                    """
            )
            await ctx.reply(embed=embed)

client.run(TOKEN)
