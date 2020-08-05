from discord.ext import commands
import os
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

def make_team(ctx):
    vc = ctx.author.voice
    members = [member.name for member in vc.channel.members]
    random.shuffle(members)

    teamA = []
    teamB = []
    nr_members = len(members)
    for i in range(nr_members):
        if i % 2 == 0:
            teamA.append(members[i])
        else:
            teamB.append(members[i])
    msg = '=== TEAM A ===\n' + '\n'.join(teamA) + '\n\n=== TEAM B ===\n' + '\n'.join(teamB)
    return msg

@bot.command()
async def team(ctx):
    msg = make_team(ctx)
    await ctx.channel.send(msg)

bot.run(token)
