import lightbulb
import hikari
import random
import string
   

commands_plugin = lightbulb.Plugin('Commands')



@commands_plugin.command
@lightbulb.add_checks(lightbulb.checks.has_guild_permissions(lightbulb.guild_only))
@lightbulb.option("amount","password length", type=int, required=True)
@lightbulb.command('genpass','Generate and store a password')
@lightbulb.implements(lightbulb.SlashCommand)
async def GenPass(ctx, amount: int):
    
    increment = 0

    if ctx.author == "649892152398315540" or ctx.author == "908230946053034015":
        increment = increment+1 
        awaiting = 4-increment 
        await ctx.respond(increment + " Users have authorised this action, awaiting" + awaiting + "authorisation commands")
       
        if increment == 4:
            await ctx.respond('Generating password, expect a DM')
                
            data = list(string.ascii_letters + string.digits + "!@#$%^&*(){},.<>/?-+=_|;:'[]")

            random.shuffle(data)

            password = []
            for i in range(amount):
                password.append(random.choice(data))

            random.shuffle(password)
            joined_password = "".join(password)
            await ctx.author.send(joined_password)
    else:
        await ctx.respond("Unauthorised to issue command")
    
    


@commands_plugin.command
@lightbulb.add_checks(lightbulb.checks.has_guild_permissions(lightbulb.guild_only))
@lightbulb.option("players", "Russian roulette players", hikari.User, required=True)
@lightbulb.command('roulette', 'How long can you and your friends last?')
@lightbulb.implements(lightbulb.SlashCommand)
async def russianRoulette(ctx: lightbulb.Context, players): 
    bullet =  random.randint(0, 6)
    

def load(bot):
    bot.add_plugin(commands_plugin)