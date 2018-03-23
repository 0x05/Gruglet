import api_lastfm
import api_youtube
import env_loader
import discord
from discord.ext import commands
import logger
import platform
from secrets import randbelow

client = commands.Bot(command_prefix='?')


@client.event
async def on_ready():
    print(f'[*] Logged in as {client.user.name}#{client.user.discriminator}')
    print(f'[*] Connected to: {str(len(client.guilds))} servers | {str(len(set(client.get_all_members())))} users')
    print(f'[*] Discord.py Version: {discord.__version__} | Python Version: {platform.python_version()}')
    print(f'[*] Invite {client.user.name}: '
          f'https://discordapp.com/oauth2/authorize?client_id={client.user.id}&scope=bot&permissions=8')
    await client.change_presence(activity=discord.Game(name='?help'))


# Generate a random roll
@client.command(usage='[max]', brief='[max]')
async def roll(ctx, *args):
    if len(args) >= 1 and args[0].isdigit():
        rnd = randbelow(int(args[0])) + 1
    else:
        rnd = randbelow(100) + 1
    await ctx.send(f'{ctx.message.author.mention} rolled {rnd}!')


# Get similar artists from last.fm
@client.command(usage='<artist> [limit]', brief='<artist> [limit]\t(Similar Artists)')
async def similar(ctx, *args):
    # Log command and author
    ca_log = f'{ctx.message.content} invoked by {ctx.message.author}'
    # Check limit
    if len(args) > 1 and args[1].isdigit() and int(args[1]) > 0:
        limit = args[1]
    else:
        # Default value if no argument is passed
        limit = 5
    # Attempt to query the API
    try:
        similar = api_lastfm.get_similar(args[0], int(limit))
    except Exception as e:
        similar = logger.log(type(e).__name__, ca_log)

    await ctx.send(similar)


# Get top tracks for an artist from last.fm
@client.command(usage='<artist> [limit]', brief='<artist> [limit]\t(Top Tracks)')
async def tt(ctx, *args):
    # Log command and author
    ca_log = f'{ctx.message.content} invoked by {ctx.message.author}'
    # Check limit
    if len(args) > 1 and args[1].isdigit() and int(args[1]) > 0:
        limit = args[1]
    else:
        # Default value if no argument is passed
        limit = 5
    # Attempt to query the API
    try:
        track = api_lastfm.get_top_tracks(args[0], int(limit))
    except Exception as e:
        track = logger.log(type(e).__name__, ca_log)

    await ctx.send(track)


# Get top albums for an artist from last.fm
@client.command(usage='<artist> [limit]', brief='<artist> [limit]\t(Top Albums)')
async def ta(ctx, *args):
    # Log command and author
    ca_log = f'{ctx.message.content} invoked by {ctx.message.author}'
    # Check limit
    if len(args) > 1 and args[1].isdigit() and int(args[1]) > 0:
        limit = args[1]
    else:
        # Default value if no argument is passed
        limit = 5
    # Attempt to query the API
    try:
        album = api_lastfm.get_top_albums(args[0], int(limit))
    except Exception as e:
        album = logger.log(type(e).__name__, ca_log)

    await ctx.send(album)


# Link to last.fm and one of artist's top tracks from YouTube
@client.command(usage='<artist>', brief='<artist>\t\t\t(Artist Info)')
async def artist(ctx, *args):
    # Log command and author
    ca_log = f'{ctx.message.content} invoked by {ctx.message.author}'
    # Attempt to query the API
    try:
        l_artist = api_lastfm.get_artist(args[0])
    except Exception as e:
        l_artist = logger.log(type(e).__name__, ca_log)
        await ctx.send(l_artist)
    else:
        if l_artist != 1:
            # Link to artist wiki
            await ctx.send(l_artist)
            # Select a random top 10 track
            select = randbelow(10)
            toptrack = api_lastfm.get_top_tracks(args[0], 10, select)
            # Search YouTube for Artist - Track
            search = f'{args[0]} - {toptrack}'
            link = api_youtube.search(search,0)
            await ctx.send(link)
        else:
            await ctx.send('Artist not found.')


# Search YouTube
@client.command(usage='<search> [result]', brief='<search> [result]   (YouTube Search)')
async def yt(ctx, *args):
    # Log command and author
    ca_log = f'{ctx.message.content} invoked by {ctx.message.author}'
    # First result by default
    result = 0
    # Select another result if specified
    if len(args) > 1 and args[1].isdigit() and int(args[1]) > 0:
        if int(args[1]) < 10:
            result = args[1]
    # Attempt to query the API
    try:
        search = api_youtube.search(args[0], int(result))
    except Exception as e:
        search = logger.log(type(e).__name__, ca_log)

    await ctx.send(search)


client.run(env_loader.DISCORD_TOKEN)
