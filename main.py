from ext.config import *
from initialext import *
import interactions
from interactions.ext.tasks import IntervalTrigger, create_task
import requests
import colorama

token = open("token.txt").readline()
bot = interactions.Client(token=token, intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGE_CONTENT | interactions.Intents.GUILD_MEMBERS)


@create_task(IntervalTrigger(120))
async def check():
    """checks SOL price every 2 minutes"""
    url = "https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT"
    data = requests.get(url)  
    data = data.json()
    print("checked")
    price = data["price"].strip("0")
    await bot.change_presence(interactions.ClientPresence(activities=[interactions.PresenceActivity(name=f"SOL: ${price}", type=interactions.PresenceActivityType.WATCHING)]))

banner = """
  ____                            _                    _
 / ___|___  _ __  _ __   ___ _ __| |__   ___  __ _  __| |
| |   / _ \| '_ \| '_ \ / _ \ '__| '_ \ / _ \/ _` |/ _` |
| |__| (_) | |_) | |_) |  __/ |  | | | |  __/ (_| | (_| |
 \____\___/| .__/| .__/ \___|_|  |_| |_|\___|\__,_|\__,_|
           |_|   |_|

    Made with ❤️  by Morgandri1
"""

print(colorama.Fore.GREEN + banner + colorama.Fore.RESET)
for ext in cogs:
    bot.load(ext)
    print("loaded " + ext)
check.start()
bot.start()