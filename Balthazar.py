import time
import os
import discord
from discord.ext import commands

from datetime import datetime
from utils import default
from utils.data import HelpFormat

config = default.get("config.json")
token = config['token']
chanelList = config['chanel']
owner = config['owner']
version = config['version']

print("Logging in...")

bot = commands.Bot(
    command_prefix='$', prefix='$',
    help_command=HelpFormat()
)


@bot.event
async def on_ready():
    await bot.get_channel(chanelList).send("Hello World!")

@bot.event
async def help(ctx):
    await ctx.send("Bjr voici les commmande:\nrien...")

@bot.event
async def on_message_delete(ctx):
    user = ctx.author
    content = ctx.content
    chanel = ctx.channel
    await chanel.send("**LOL** regardez le ! " + str(user) + " a essayé de supprimer sont message: " + content +"\n**Quel petite pu****")

@bot.command()
async def money(ctx):
    await ctx.send("Thank you for your donation")

@bot.command()
async def miroir(ctx, argv):
    await ctx.send(argv)

@bot.command()
async def serveurInfo(ctx):
    server = ctx.guild
    number_of_text_channels = len(server.text_channels)
    number_of_voice_channels = len(server.voice_channels)
    server_description = server.description
    number_of_person = server.member_count
    server_name = server.name
    message = f"Le serveur {server_name} contient {number_of_person} personnes.\nLa description de serveur {server_description}.\nCe serveur possède {number_of_text_channels} salons écrit ainsi que {number_of_voice_channels} salons vocaux."
    await ctx.send(message)

@bot.command(aliases=['info', 'stats', 'status'])
async def about(ctx):
    """ About the bot """
    #ramUsage = process.memory_full_info().rss / 1024**2
    avgmembers = round(len(bot.users) / len(bot.guilds))

    embedColour = discord.Embed.Empty
    if hasattr(ctx, 'guild') and ctx.guild is not None:
        embedColour = ctx.me.top_role.colour

    embed = discord.Embed(colour=embedColour)
    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
    #embed.add_field(name="Last boot", value=default.timeago(datetime.now() - bot.uptime), inline=True)
    embed.add_field(
        name=f"Developer",
        value=''.join(owner),
        inline=True)
    embed.add_field(name="Library", value="discord.py", inline=True)
    embed.add_field(name="Servers", value=f"{len(ctx.bot.guilds)} ( avg: {avgmembers} users/server )", inline=True)
    embed.add_field(name="Commands loaded", value=len([x.name for x in bot.commands]), inline=True)
    #embed.add_field(name="RAM", value=f"{ramUsage:.2f} MB", inline=True)

    await ctx.send(content=f"ℹ About **{ctx.bot.user}** | **{version}**", embed=embed)


if __name__ == '__main__':
    for file in os.listdir("src"):
        if file.endswith(".py"):
            name = file[:-3]
            bot.load_extension(f"src.{name}")

    try:
        bot.run(token)
    except Exception as e:
        print(f'Error when logging in: {e}')

