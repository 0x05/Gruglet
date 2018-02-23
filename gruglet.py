import api_lastfm
import api_youtube
import env_loader
import discord
from discord.ext import commands
import platform

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():

    print(f'[*] Logged in as {client.user.name}#{client.user.discriminator}')
    print(f'[*] Connected to: {str(len(client.guilds))} servers | {str(len(set(client.get_all_members())))} users')
    print(f'[*] Discord.py Version: {discord.__version__} | Python Version: {platform.python_version()}')
    print(f'[*] Invite {client.user.name}: '
          f'https://discordapp.com/oauth2/authorize?client_id={client.user.id}&scope=bot&permissions=8')
    await client.change_presence(game=discord.Game(name='with packets'))


@client.command()
async def similar(ctx, *args):
    if len(args) > 1 and args[1].isdigit():
        limit = args[1]
    else:
        # Default value if no argument is passed
        limit = 5

    similar = api_lastfm.get_similar(args[0], int(limit))
    await ctx.send(similar)


@client.command()
async def artist(ctx, *args):
    artist = api_lastfm.get_artist(args[0])
    await  ctx.send(artist)

@client.command()
async def top(ctx, *args):
    if len(args) > 1 and args[1].isdigit():
        limit = args[1]
    else:
        # Default value if no argument is passed
        limit = 5

    track = api_lastfm.get_top_tracks(args[0], int(limit))
    await ctx.send(track)

@client.command()
async def yt(ctx, *args):
    # First result by default
    result = 0
    # Select another result if specified
    if len(args) > 1 and args[1].isdigit():
        if int(args[1]) < 10:
            result = args[1]

    search = api_youtube.search(args[0], int(result))
    await ctx.send(search)

client.run(env_loader.DISCORD_TOKEN)
