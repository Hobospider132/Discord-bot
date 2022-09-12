import lightbulb
import hikari
import datetime

plugin = lightbulb.Plugin('Ping')


@plugin.command
@lightbulb.command('ping','play ping pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

@plugin.command
@lightbulb.command('invite','displays bot invite link')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('The bots invite link is\nhttps://discord.com/api/oauth2/authorize?client_id=1007271737228009492&permissions=3072&scope=bot')

@plugin.command
@lightbulb.command('help','shows commands')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('/ping will ping the bot, /help will show all commands, /genpass will generate and store a password, /invite displays the bots invite link')

@plugin.command
@lightbulb.command('responsetime','measures bots response time')
@lightbulb.implements(lightbulb.SlashCommand)
async def responsetime(ctx: lightbulb.Context) -> None:
    heartbeat = ctx.bot.heartbeat_latency * 1000
    txt = (f":timer::timer_clock: Reponse time")

    if isinstance(ctx, lightbulb.PrefixContext):
        if ctx.invoked_with == "pong":
            txt = (f":ping_pong: Ping!")

    if heartbeat > 1000:
        colours = hikari.Colour(0xFF0000)
    elif heartbeat > 500:
        colours = hikari.Colour(0xFFFF00)
    else:
        colours = hikari.Colour(0x26D934)
    
    ping= hikari.Embed(
            title="Current Response Time:",
            description=f"```💓: {heartbeat:,.2f}ms.```",
            timestamp=datetime.datetime.now().astimezone(),
            color=colours,
        )
    await ctx.respond(embed=ping, content=txt)

def load(bot):
    bot.add_plugin(plugin)