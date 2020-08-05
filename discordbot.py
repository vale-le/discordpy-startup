from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

def make_team(ctx, nr_team):
    vc = ctx.author.voice
    members = [member.name for member in vc.channel.members]

    return members

@bot.command()
async def team(ctx, nr_team=2):
    msg = make_team(ctx, nr_team)
    await ctx.channel.send(msg)

bot.run(token)
