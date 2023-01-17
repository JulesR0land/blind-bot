from random import shuffle
from pytube import Playlist
from discord import FFmpegPCMAudio, Client, Intents
from asyncio import run_coroutine_threadsafe
from asyncio import sleep as async_sleep


from ytUtils import get_yt_url_infos
from blindGlobals import blindGlobals, globals, BOT_INTENTS, CONST_FFMPEG_OPTIONS

from pafy import new


client = Client(intents=BOT_INTENTS)


async def get_voice_channel(ctx):
    global globals

    if not globals[ctx.guild.id].playlist_url:
        await ctx.send("Please set a playlist with the \"!setPlaylist\" command before playing.")
        return

    channel = ctx.author.voice.channel

    if not channel:
        await ctx.send("You need to be connected to a vocal channel.")
    elif not ctx.voice_client:
        globals[ctx.guild.id].channel_id = await channel.connect()


async def shuffle_playlist(ctx):
    try:
        list_url = list(Playlist(globals[ctx.guild.id].playlist_url))
    except:
        await ctx.send("Please use a valid playlist url.")
        return None

    shuffle(list_url)
    return list_url


def check_existing_audio(url):
    audio = get_yt_audio(url)

    if not audio:
        path, title = dl_yt_audio(url)
        add_yt_audio(url, title, path)
    else:
        path = audio[2]
        title = audio[1]

    return path, title


async def prepare_next_audio(guild_id, main_loop):
    global globals

    url = globals[guild_id].audio_queue[globals[guild_id].current_audio]
    video_infos = get_yt_url_infos(url)

    await globals[guild_id].play_channel.send(
        "```Title: " +
        video_infos["title"] +
        "\nUrl: " +
        video_infos["webpage_url"] +
        "```")

    globals[guild_id].current_audio += 1

    if globals[guild_id].stopped:
        globals[guild_id].stopped = False
        await globals[guild_id].play_channel.send("Stopping the blind test, thanks for playing !")
        return

    if len(globals[guild_id].audio_queue) <= globals[guild_id].current_audio:
        await globals[guild_id].play_channel.send("End of the blind test, thanks for playing !")
        globals[guild_id].current_audio = -1
        return

    await async_sleep(3)
    await start_blind_test(guild_id, main_loop)


async def start_blind_test(guild_id, main_loop):

    url = globals[guild_id].audio_queue[globals[guild_id].current_audio]

    video = new(url)
    best = video.getbestaudio()
    play_url = best.url

    ffmpeg_options = CONST_FFMPEG_OPTIONS
    ffmpeg_options["options"] += f" -t {globals[guild_id].time_per_audio}"
    source = FFmpegPCMAudio(play_url, **ffmpeg_options)

    globals[guild_id].channel_id.play(source, after=lambda e : run_coroutine_threadsafe(prepare_next_audio(guild_id, main_loop), main_loop))

    globals[guild_id].stopped = False


def check_server_id(ctx):
    global globals

    if not ctx.guild.id in globals:
        globals[ctx.guild.id] = blindGlobals()