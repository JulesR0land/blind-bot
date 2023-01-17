
from discord import Intents


class blindGlobals():
    def __init__(self):
        self.channel_id = None

        self.playlist_url = "https://www.youtube.com/playlist?list=PLj4MZ0eMNwxNK5IQEY7qWkKy8Ez_FpBJ7"
        self.audio_queue = []
        self.current_audio = -1
        self.play_channel = None
        self.stopped = False

        self.time_per_audio = 15
        self.title_tts = False


globals = {}

BOT_INTENTS = Intents.default()
BOT_INTENTS.members = True
BOT_INTENTS.messages = True
BOT_INTENTS.message_content = True

CONST_FFMPEG_OPTIONS = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn"
}

help_infos = {
    "bonjour": [
        "Say hi to the bot",
        "It's nice to greet the bot, thanks"
    ],
    "setPlaylist": [
        "Use an url to set a playlist to play",
        "setPlaylist \"url\" - Take 1 url to set the playlist you want to be played\n" +
        "The default is a test playlist: https://www.youtube.com/playlist?list=PLj4MZ0eMNwxNK5IQEY7qWkKy8Ez_FpBJ7"
    ],
    "setTime": [
        "Set the time played for each audio",
        "setTime \"integer\" - Take 1 integer to set the time played for each audio\n" +
        "The default is 15 seconds"
    ],
    "setTTS": [
        "Enable the TTS for the title of each audio (Not working properly)",
        "Enable the TTS for the title of each audio (Not working properly)\n" +
        "Disabled by default"
    ],
    "unsetTTS": [
        "Disable the TTS for the title at the end each audio (Not working properly)",
        "Disable the TTS for the title at the end each audio (Not working properly)\n" +
        "Disabled by default"
    ],
    "parameters": [
        "Show every parameters and their value",
        "Show every parameters and their value"
    ],
    "play": [
        "Play the playlist randomly",
        "Play the playlist randomly and write the title and url at the end of each audio"
    ],
    "pause": [
        "Pause the current playing audio",
        "Pause the current playing audio"
    ],
    "resume": [
        "Resume the current paused audio",
        "Resume the current paused audio"
    ],
    "skip": [
        "Skip the current playing audio",
        "Skip the current playing audio"
    ],
    "stop": [
        "Stop the current playing audio",
        "Stop the current playing audio"
    ],
    "leave": [
        "Make the bot leaving the vocal channel",
        "Make the bot leaving the vocal channel\n" +
        "printing the title of the song currently played if any"
    ]
}