import discord
from discord.ext import commands
import datetime
import os
import random
import re
import traceback

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


# @bot.event
# async def on_command_error(ctx, error):
#     orig_error = getattr(error, "original", error)
#     error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#     await ctx.send(error_msg)


@bot.command()
async def team(ctx, *adj):
    msg = make_team(ctx, adj)
    await ctx.channel.send(msg)


@bot.command()
async def lint(ctx):
    champs = ['モルデ', 'ダリウス', 'フィオラ', 'イラオイ', 'ヘカリム', 'グレイブス', 'ボリベア']
    champ = random.choice(champs)
    msg = 'Lint さんは {} を使ってください'.format(champ)
    await ctx.channel.send(msg)

    
@bot.command()
async def arai(ctx):
    arai_pass = ['yuuya3838', 'araiyuuya3838']
    p = random.choice(arai_pass)
    await ctx.channel.send(p)


@bot.command()
async def mcd(ctx):
    reg = ['ハンバーガー', 'チーズバーガー', 'チキンクリスプ', 'ベーコンマックポーク', 'チキンチーズバーガー',
           'チキンチーズバーガー', 'エッグチーズバーガー', 'スパイシーチーズバーガー', 'えびフィレオ', 'ベーコンレタスバーガー',
           'てりやきチキンフィレオ', 'フィレオフィッシュ', 'てりやきマックバーガー', 'ダブルチーズバーガー', 'グラン ベーコンチーズ',
           'グラン クラブハウス', 'ビッグマック']
    night = ['倍ビッグマック', '倍グラン クラブハウス', '倍グラン ベーコンチーズ', '倍ダブルチーズバーガー', '倍てりやきマックバーガー',
             '倍フィレオフィッシュ', '倍チキンフィレオ', '倍てりやきチキンフィレオ', '倍ベーコンレタスバーガー', '倍えびフィレオ',
             '倍スパイシーチキンバーガー', '倍エッグチーズバーガー', '倍チキンチーズバーガー', '倍ベーコンマックポーク', '倍ハンバーガー',
             '倍チキンクリスプ', '倍チーズバーガー']
    promo = ['ハワイアンスパイシーバーベキュー', 'ガーリックシュリンプ', 'チーズロコモコ']
    morning = ['エッグマックマフィン', 'ベーコンエッグマックサンド', 'ソーセージエッグマフィン', 'ソーセージマフィン',
               'チキンクリスプマフィン', 'フィレオフィッシュ', 'ホットケーキ', 'マックグリドル ソーセージエッグ',
               'マックグリドル ベーコンエッグ', 'マックグリドル ソーセージ', 'メガマフィン', 'ビッグブレックファスト']

    created_time = ctx.message.created_at.time()
    morning_time = datetime.time(20)
    lunch_time = datetime.time(1, 30)
    dinner_time = datetime.time(8)

    if created_time > morning_time or created_time <= lunch_time:
        burger = random.choice(morning)
    elif created_time > lunch_time and created_time <= dinner_time:
        burger = random.choice(reg + promo)
    elif created_time > dinner_time and created_time <= morning_time:
        burger = random.choice(reg + night + promo)

    await ctx.channel.send(burger)


@bot.command()
async def sadao(ctx):
    await ctx.channel.send('0202')


@bot.command()
async def atsushi(ctx):
    await ctx.channel.send('0202')


@bot.command()
async def kfc(ctx):
    await ctx.channel.send('マック行け')


@bot.command()
async def mos(ctx):
    await ctx.channel.send('スパイシーモスチーズバーガー')


@bot.command()
async def lane(ctx):
    ls = ['top', 'adc', 'jungle', 'mid', 'support', 'lint']
    l = random.choice(ls)
    await ctx.channel.send(l)


@bot.command()
async def aram(ctx):
    all_cmp = ['アーゴット', 'アーリ', 'アイバーン', 'アカリ', 'アジール', 'アッシュ',
               'アニー', 'アニビア', 'アフェリオス', 'アムム', 'アリスター', 'イブリン',
               'イラオイ', 'イレリア', 'ウーコン', 'ウディア', 'エイトロックス', 'エコー',
               'エズリアル', 'エリス', 'オーン', 'オラフ', 'オリアナ', 'オレリオン・ソル',
               'カーサス', 'カ＝ジックス', 'カイ＝サ', 'カサディン', 'カシオペア', 'カタリナ',
               'カミール', 'カリスタ', 'カルマ', 'ガリオ', 'ガレン', 'ガングプランク', 'キヤナ',
               'キンドレッド', 'クイン', 'クレッド', 'グラガス', 'グレイブス', 'ケイトリン',
               'ケイル', 'ケイン', 'ケネン', 'コーキ', 'コグ＝マウ', 'サイオン', 'サイラス',
               'ザイラ', 'ザック', 'ザヤ', 'シェン', 'シャコ', 'シン・ジャオ', 'シンジド', 
               'シンドラ', 'シヴァーナ', 'シヴィア', 'ジェイス', 'ジグス', 'ジャーヴァンIV',
               'ジャックス', 'ジャンナ', 'ジリアン', 'ジン', 'ジンクス', 'スウェイン',
               'スカーナー', 'スレッシュ', 'セジュアニ', 'セト', 'セナ', 'ゼド', 'ゼラス',
               'ソナ', 'ソラカ', 'ゾーイ', 'タム・ケンチ', 'タリック', 'タリヤ', 'タロン',
               'ダイアナ', 'ダリウス', 'チョ＝ガス', 'ツイステッド・フェイト', 'ティーモ',
               'トゥイッチ', 'トランドル', 'トリスターナ', 'トリンダメア', 'ドクター・ムンド',
               'ドレイヴン', 'ナー', 'ナサス', 'ナミ', 'ニーコ', 'ニダリー', 'ヌヌ＆ウィルンプ',
               'ノーチラス', 'ノクターン', 'ハイマーディンガー', 'バード', 'パイク', 'パンテオン',
               'ビクター', 'フィオラ', 'フィズ', 'フィドルスティックス', 'ブラウム', 'ブラッドミア',
               'ブランド', 'ブリッツクランク', 'ヘカリム', 'ベイガー', 'ボリベア', 'ポッピー',
               'マオカイ', 'マスター・イー', 'マルザハール', 'マルファイト', 'ミス・フォーチュン',
               'モルガナ', 'モルデカイザー', 'ヤスオ', 'ユーミ', 'ヨリック', 'ヨネ', 'ライズ', 'ラカン',
               'ラックス', 'ラムス', 'ランブル', 'リー・シン', 'リサンドラ', 'リリア', 'リヴェン',
               'ルシアン', 'ルブラン', 'ルル', 'レオナ', 'レク＝サイ', 'レネクトン', 'レンガー',
               'ワーウィック', 'ヴァイ', 'ヴァルス', 'ヴェイン', 'ヴェル＝コズ'
               ]
    champ = random.choice(all_cmp)
    msg = '{} さんは {} を使ってください'.format(ctx.author.name, champ)
    await ctx.channel.send(msg)


bot.run(token)
