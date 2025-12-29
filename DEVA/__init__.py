# Authored By Certified Coders © 2025
from DEVA.core.bot import MusicBotClient
from DEVA.core.dir import StorageManager
from DEVA.core.git import git
from DEVA.core.userbot import Userbot
from DEVA.misc import dbb, heroku
from DEVA.logging import LOGGER

StorageManager()
git()
dbb()
heroku()

app = MusicBotClient()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
