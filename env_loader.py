import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Load tokens
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
LASTFM_KEY = os.environ.get("LASTFM_KEY")
YT_KEY = os.environ.get("YT_KEY")
