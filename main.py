import discord
import sys
import time

bot = discord.Bot()

@bot.message_command(name="Show Account Age", description="Show the account age of this user")
async def accountagemsg(ctx, message):
    author = "<@"+str(message.author.id)+">"
    timestamp = message.author.created_at
    await ctx.respond("Creation date of "+author+" was <t:"+str(time.mktime(timestamp.timetuple()))[:-2]+":R>"+" on <t:"+str(time.mktime(timestamp.timetuple()))[:-2]+":d>", ephemeral=True)

@bot.slash_command(description="Show the account age of a user")
async def accountage(ctx, user : discord.User):
    timestamp = user.created_at
    author = "<@"+str(user.id)+">"
    await ctx.respond("Creation date of "+author+" was <t:"+str(time.mktime(timestamp.timetuple()))[:-2]+":R>"+" on <t:"+str(time.mktime(timestamp.timetuple()))[:-2]+":d>", ephemeral=True)

@bot.user_command(description="Shows the account age of this user", name="Show Account Age")
async def useraccountage(ctx, user : discord.User):
    timestamp = user.created_at
    author = "<@"+str(user.id)+">"
    await ctx.respond("Creation date of "+author+" was <t:"+str(time.mktime(timestamp.timetuple()))[:-2]+":R>"+" on <t:"+str(time.mktime(timestamp.timetuple()))[:-2]+":d>", ephemeral=True)

bot.run(sys.argv[1])
