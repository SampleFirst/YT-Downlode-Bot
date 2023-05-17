import os

class Config(object):
  
# API credentials
API_ID = int(os.environ.get("API_ID", 23906038))
API_HASH = os.environ.get("API_HASH" "dff1eb42fad7971f16da662a99c0f376")

# Bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5891308865:AAHK-iw8PiSLOHEDF6JqmVRiQmj43uYXFnA")

# Directory for storing downloaded files
DOWNLOADS_DIR = 'downloads'
