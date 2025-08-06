from os import environ 

class Config:
    API_ID = environ.get("API_ID", "29756601")
    API_HASH = environ.get("API_HASH", "967c4656b8dd6a475b7786e3287ba2d3")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7636592246:AAH4c6CelIHlJK7_MV8YCWpi5P4QAYH3x2I") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://whatsapp110x:whatsapp110x@cluster0.dh2ygtt.mongodb.net/sample_mflix?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7052170756').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
