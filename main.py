from bot import Bot
from keep_alive import keep_alive

keep_alive()  # Keeps the bot alive on free Render

app = Bot()
app.run()
