from discord.ext import commands
import os
import random
import re

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

def make_team(ctx, adj):
    include = []
    exclude = []
    for mem in adj:
        if re.match(r'\+.+', mem):
            include.append(mem[1:])
        elif re.match(r'\-.+', mem):
            exclude.append(mem[1:])
    vc = ctx.author.voice
    members = list(({member.name for member in vc.channel.members} | set(include)) - set(exclude))
    random.shuffle(members)

    teamA = []
    teamB = []
    nr_members = len(members)
    for i in range(nr_members):
        if i % 2 == 0:
            teamA.append(members[i])
        else:
            teamB.append(members[i])
    msg = '.\n=== グリフィンドール ===\n' + '\n'.join(teamA) + '\n\n=== スリザリン ===\n' + '\n'.join(teamB)
    return msg

@bot.command()
async def team(ctx, *adj):
    msg = make_team(ctx, adj)
    await ctx.channel.send(msg)


@bot.command()
async def lint(ctx):
    champs = ['モルデ', 'ダリウス', 'フィオラ', 'イラオイ', 'ヘカリム', 'グレイブス','ブラッドミア']
    champ = random.choice(champs)
    msg = 'Lint さんは {} を使ってください'.format(champ)
    await ctx.channel.send(msg)

@bot.command()
async def arai(ctx):
    await ctx.channel.send('yuya3838')

bot.run(token)
