from discord.ext import commands
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


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


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


@bot.command()
async def random(ctx):
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
               'モルガナ', 'モルデカイザー', 'ヤスオ', 'ユーミ', 'ヨリック', 'ライズ', 'ラカン',
               'ラックス', 'ラムス', 'ランブル', 'リー・シン', 'リサンドラ', 'リリア', 'リヴェン',
               'ルシアン', 'ルブラン', 'ルル', 'レオナ', 'レク＝サイ', 'レネクトン', 'レンガー',
               'ワーウィック', 'ヴァイ', 'ヴァルス', 'ヴェイン', 'ヴェル＝コズ'
               ]
    champ = random.choice(all_cmp)
    mgs = 'は {} を使ってください'.format(champ)
    await ctx.channel.send(msg)


bot.run(token)
