from discord.ext import commands
import os
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

def make_team(ctx, exclude):
    vc = ctx.author.voice
    members = list({member.name for member in vc.channel.members} - set(exclude))
    random.shuffle(members)

    teamA = []
    teamB = []
    nr_members = len(members)
    for i in range(nr_members):
        if i % 2 == 0:
            teamA.append(members[i])
        else:
            teamB.append(members[i])
    msg = '.\n=== TEAM A ===\n' + '\n'.join(teamA) + '\n\n=== TEAM B ===\n' + '\n'.join(teamB)
    return msg

@bot.command()
async def team(ctx, *exclude):
    msg = make_team(ctx, exclude)
    await ctx.channel.send(msg)


@bot.command()
async def lint(ctx):
    champs = ['モルデ', 'ダリウス', 'フィオラ', 'イラオイ', 'ヘカリム', 'グレイブス']
    champ = random.choice(champs)
    msg = 'Lint さんは {} を使ってください'.format(champ)
    await ctx.channel.send(msg)

@bot.command()
async def arai(ctx):
    await ctx.channel.send('yuya3838')

bot.run(token)
