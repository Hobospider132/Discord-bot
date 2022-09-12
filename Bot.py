import lightbulb
import hikari
from random import choice
from utils.statuses import statuses
from utils.stats import INTENTS, TOKEN


bot = lightbulb.BotApp(TOKEN, INTENTS)

bot.load_extensions_from('./extensions')
bot.load_extensions_from('./handlers')
bot.run(        
        status=hikari.Status.ONLINE,
        activity=hikari.Activity(
            name=choice(statuses),
            type=hikari.ActivityType.PLAYING)
            )