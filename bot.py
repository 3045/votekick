import discord, time
from discord.ext import commands

bot = commands.Bot(command_prefix='-')
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'logged in as {bot.user} ({bot.user.id})')

@bot.command()
async def votekick(ctx, lol: discord.Member):
    if lol.id == bot.user.id:
        await ctx.reply("cant kick me")
        return
    msg = await ctx.reply(f"kick {lol.mention}? (3 votes required)")
    await msg.add_reaction("👍")
@bot.event 
async def on_reaction_add(reaction, user):
    expiresAt = int(time.mktime(reaction.message.created_at.timetuple())+300)
    timeNow = int(time.time())
    if timeNow >= expiresAt:
        return await reaction.message.edit(content=f"this votekick has expired.")
    if reaction.count == 4 and reaction.emoji == "👍":
        await reaction.message.delete()
        try:
            await lol.kick()
            await ctx.send(f"later, {lol.mention}")
        except:
            await ctx.send("cannot kick this user (higher role?)")
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.reply("invalid argument")

bot.run('BOTTOKENHERE')
