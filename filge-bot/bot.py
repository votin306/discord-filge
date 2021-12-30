import discord
from discord.ext import commands
from config import settings
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL
import os

client = commands.Bot(command_prefix = settings['prefix'])

@client.event
async def on_ready():
    print(f"{settings['bot']} готов к работе")

@client.command() 
async def purge(ctx, limit: int): 
    author = ctx.message.author 
    if(author.guild_permissions.manage_messages or author.guild_permissions.administrator):
        if(limit < 101):
            await ctx.channel.purge(limit=limit)
        else:
            await ctx.send('Аргумент limit больше 100. Попробуй &delete 100')
    else:
        embed=discord.Embed(title="Ты че?", description="У тебя нету прав удалять сообщения. Пацан к успеху шел :(", color=0x1fcae0)
        await ctx.send(embed=embed)

@client.command() 
async def say(ctx, *, text): 
    if("<" in text and ">" in text):
        await ctx.channel.purge(limit=1)
        await ctx.send("К сожалению ты в сообщении имеешь пинг или тому подобное. Я не могу это отправить :(")
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send(text)

@client.command() 
async def kick(ctx, member: discord.Member, *, reason=None): 
    if(author.guild_permissions.kick_members or author.guild_permissions.administrator):
        await ctx.send(f"{member} был нах** от сюда выкинут :))")
        await member.kick(reason=reason)
    else:
        embed=discord.Embed(title="Ты че?", description="У тебя нету прав удалять сообщения. Пацан к успеху шел :(", color=0x1fcae0)
        await ctx.send(embed=embed)


@client.command() 
async def join(message):
    ##Connect to channel
    connection = message.author.guild.voice_client
    idUserChannel = message.author.voice.channel.id
    idBotChannel = 0
    if connection:
        idBotChannel = client.voice_clients[0].channel.id
    if (connection) and (idBotChannel != idUserChannel) :
        await message.channel.send('**Moving to** ' + str(message.author.voice.channel))
        await connection.move_to(message.author.voice.channel)
    elif (idBotChannel != idUserChannel):
        await message.channel.send('**Connect to** ' + str(message.author.voice.channel))
        await message.author.voice.channel.connect()

@client.command() 
async def play(ctx,video_link, voice, message):
    ##Воспроизведение песенок
    ydl_opts = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_link, download = False)
    print(info.get('title'))
    URL = info['formats'][0]['url']
    voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after = lambda e: myAfter(voice, message))
    voice.is_playing()
    await message.channel.send('**Сейчас играет** - ' + info.get('title'))

@client.command()
async def myAfter(voice, message):
    coro = await musicQueue(voice, message)
    asyncio.run_coroutine_threadsafe(coro).result()

@client.command() 
async def skip(voice, message):
    ##Skip
    voice.stop()
    await serverQueue(voice, message)
    await message.channel.send('**Successfully skiped** - ' + info.get('title'))
    
##Queue
queue = []
@client.command() 
async def serverQueue(voice, message):
    if queue != [] and not voice.is_playing():
        await play(queue.pop(0), voice, message)
        print('queue - ' + str(queue))

queue = []
async def serverQueue(voice, message):
    if queue != [] and not voice.is_playing():
        await play(queue.pop(0), voice, message)
        print('queue - ' + str(queue))

client.run(settings['token']) 
