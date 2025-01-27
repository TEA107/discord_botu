import os
from dotenv import load_dotenv
load_dotenv(override=True)

TOKEN = os.environ.get("DISCORD_TOKEN")
CURRENCY_TOKEN = os.environ.get("CURRENCY_TOKEN")

import requests

import discord
from discord.ext import commands

izinler = discord.Intents.default()
izinler.message_content = True

bot = commands.Bot(command_prefix="!", intents = izinler)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.lower().startswith("hello"):
        await message.channel.send(f"hello, my name is {bot.user.name}")

    if message.content.lower().startswith("babamin adi ne"):
        await message.channel.send(f"harun")

    if message.content.lower().startswith("en buyuk kuzenimin adi ne"):
        await message.channel.send(f"beyza")

    if message.content.lower().startswith("en kucuk kuzenimin adi ne"):
        await message.channel.send(f"defne")
    
    if message.content.lower().startswith("ortanca kuzenimin adi ne"):
        await message.channel.send(f"beren")

    if message.content.lower().startswith("yengemin adi ne"):
        await message.channel.send(f"ayse")

    if message.content.lower().startswith("dayimin adi ne"):
        await message.channel.send(f"mustafa")

    if message.content.lower().startswith("anneannemin adi ne"):
        await message.channel.send(f"sukran")

    if message.content.lower().startswith("kardesimin adi ne"):
        await message.channel.send(f"gokhan")

    if message.content.lower().startswith("baba tarafindan dedemin adi ne"):
        await message.channel.send(f"halil")

    if message.content.lower().startswith("anne tarafindan dedemin adi ne"):
        await message.channel.send(f"huseyin")

    if message.content.lower().startswith("annemin adi ne"):
        await message.channel.send(f"berna")

    if message.content.lower().startswith("benim adim ne"):
        await message.channel.send(f"turkay")

    if message.content.lower().startswith("dunyanin en iyi futbolcusu kim"):
        await message.channel.send(f"ronaldo")
    await bot.process_commands(message)



@bot.command("topla")
async def topla(ctx, sayi1, sayi2):
    toplam = int(sayi1) + int(sayi2)
    await ctx.send(f"{sayi1} + {sayi2} = {toplam}")

@bot.command("bol")
async def bol(ctx, sayi3, sayi4):
    bolum = int(sayi3) / int(sayi4)
    await ctx.send(f"{sayi3} / {sayi4} = {bolum}")

@bot.command("carp")
async def carp(ctx, sayi5, sayi6):
    carpim = int(sayi5) * int(sayi6)
    await ctx.send(f"{sayi5} * {sayi6} = {carpim}")

@bot.command("cikar")
async def cikar(ctx, sayi7, sayi8):
    cikarim = int(sayi7) - int(sayi8)
    await ctx.send(f"{sayi7} - {sayi8} = {cikarim}")

@bot.command("toplatopla")
async def toplatopla(ctx, sayi1, sayi2, sayi3):
    toplatoplaim = int(sayi1) + int(sayi2) + int(sayi3)
    await ctx.send(f"{sayi1} + {sayi2} + {sayi3} = {toplatoplaim}")

@bot.command("toplacikar")
async def toplacikar(ctx, sayi1, sayi2, sayi3):
    toplacikarim = int(sayi1) + int(sayi2) - int(sayi3)
    await ctx.send(f"{sayi1} + {sayi2} - {sayi3} = {toplacikarim}")

@bot.command("toplacarp")
async def toplacarp(ctx, sayi1, sayi2, sayi3):
    toplacarpim = int(sayi1) + int(sayi2) * int(sayi3)
    await ctx.send(f"{sayi1} + {sayi2} * {sayi3} = {toplacarpim}")

@bot.command("toplabol")
async def toplabol(ctx, sayi1, sayi2, sayi3):
    toplabolim = int(sayi1) + int(sayi2) / int(sayi3)
    await ctx.send(f"{sayi1} + {sayi2} / {sayi3} = {toplabolim}")

@bot.command("cikartopla")
async def cikartopla(ctx, sayi1, sayi2, sayi3):
    cikartoplaim = int(sayi1) - int(sayi2) + int(sayi3)
    await ctx.send(f"{sayi1} - {sayi2} + {sayi3} = {cikartoplaim}")

@bot.command("cikarcikar")
async def cikarcikar(ctx, sayi1, sayi2, sayi3):
    cikarcikarim = int(sayi1) - int(sayi2) - int(sayi3)
    await ctx.send(f"{sayi1} - {sayi2} - {sayi3} = {cikarcikarim}")

@bot.command("cikarcarp")
async def cikarcarp(ctx, sayi1, sayi2, sayi3):
    cikarcarpim = int(sayi1) - int(sayi2) * int(sayi3)
    await ctx.send(f"{sayi1} - {sayi2} * {sayi3} = {cikarcarpim}")


@bot.command("cikarbol")
async def cikarbol(ctx, sayi1, sayi2, sayi3):
    cikarbolim = int(sayi1) - int(sayi2) / int(sayi3)
    await ctx.send(f"{sayi1} - {sayi2} / {sayi3} = {cikarbolim}")

@bot.command("fulltopla")
async def fulltopla(ctx, *sayilar):
    fulltoplaim = 0
    for i in range (len(sayilar)):
        fulltoplaim  += int(sayilar[i])
    await ctx.send(f"{fulltoplaim}")

@bot.command("fullcikar")
async def fullcikar(ctx, *sayilar):
    fullcikarim = 0
    for i in range (len(sayilar)):
        fullcikarim  -= int(sayilar[i])
    await ctx.send(f"{fullcikarim}")

@bot.command("fullcarp")
async def fullcarp(ctx, *sayilar):
    fullcarpim = 0
    for i in range (len(sayilar)):
        fullcarpim  *= int(sayilar[i])
    await ctx.send(f"{fullcarpim}")

@bot.command("fullbol")
async def fullbol(ctx, *sayilar):
    fullbolim = 0
    for i in range (len(sayilar)):
        fullbolim  /= int(sayilar[i])
    await ctx.send(f"{fullbolim}")

@bot.command("not")
async def not_al(ctx, *words):
    yazi = ""
    for word in words:
        yazi += f"{word} " 
    with open(f"{words[0]}.txt", "w") as doc:
        doc.write(yazi)
    await ctx.send("yazi kaydedildi")

import random

meme_list = os.listdir("./memes")
@bot.command("meme")
async def meme(ctx):
    meme = random.choice(meme_list)
    path = os.path.join(f"./memes/{meme}")
    with open(path, "rb") as doc:
        file = discord.File(doc)
    await ctx.send(file = file)

futbolcu_list = os.listdir("./futbol")
@bot.command("futbolcu")
async def meme(ctx):
    futbolcu = random.choice(futbolcu_list)
    path = os.path.join(f"./futbol/{futbolcu}")
    with open(path, "rb") as doc:
        file = discord.File(doc)
    await ctx.send(file = file)

ulke_list = os.listdir("./ulkeler")
@bot.command("ulke")
async def ulke(ctx):
    ulke = random.choice(ulke_list)
    path = os.path.join(f"./ulkeler/{ulke}")
    with open(path, "rb") as doc:
        file = discord.File(doc)
    await ctx.send(file = file)

motivasyon_list = os.listdir("./motivasyonlar")
@bot.command("motivasyon")
async def motivasyon(ctx):
    motivasyon = random.choice(motivasyon_list)
    path = os.path.join(f"./motivasyonlar/{motivasyon}")
    with open(path, "rb") as doc:
        file = discord.File(doc)
    await ctx.send(file = file)

takim_list = os.listdir("./takimlar")
@bot.command("takim")
async def takim(ctx):
    takim = random.choice(takim_list)
    path = os.path.join(f"./takimlar/{takim}")
    with open(path, "rb") as doc:
        file = discord.File(doc)
    await ctx.send(file = file)

gezegen_list = os.listdir("./gezegenler")
@bot.command("gezegen")
async def gezegen(ctx):
    gezegen = random.choice(gezegen_list)
    path = os.path.join(f"./gezegenler/{gezegen}")
    with open(path, "rb") as doc:
        file = discord.File(doc)
    await ctx.send(file = file)

baskan_list = os.listdir("./baskanlar")
@bot.command("baskan")
async def baskan(ctx):
    baskan  = random.choice(baskan_list)
    path = os.path.join(f"./baskanlar/{baskan}")
    with open(path, "rb") as doc:
        file = discord.File(doc)
    await ctx.send(file = file)

satranc_list = os.listdir("./satranclar")
@bot.command("satranc")
async def satranc(ctx):
    satranc = random.choice(satranc_list)
    path = os.path.join(f"./satranclar/{satranc}")
    with open(path, "rb") as doc:
        file = discord.File(doc)
    await ctx.send(file = file)

gm_list = os.listdir("./gmler")
@bot.command("gm")
async def gm(ctx):
    gm = random.choice(gm_list)
    path = os.path.join(f"./gmler/{gm}")
    with open(path, "rb") as doc:
        file = discord.File(doc)
    await ctx.send(file = file)


hayvan_list = os.listdir("./hayvanlar")
@bot.command("hayvan")
async def hayvan(ctx):
    hayvan = random.choice(hayvan_list)
    path = os.path.join(f"./hayvanlar/{hayvan}")
    with open(path, "rb") as doc:
        file = discord.File(doc)
    await ctx.send(file = file)

yazar_list = os.listdir("./yazarlar")
@bot.command("yazar")
async def yazar(ctx):
    yazar = random.choice(yazar_list)
    path = os.path.join(f"./yazarlar/{yazar}")
    with open(path, "rb") as doc:
        file = discord.File(doc)
    await ctx.send(file = file)

oyuncu_list = os.listdir("./oyuncular")
@bot.command("oyuncu")
async def oyuncu(ctx):
    oyuncu = random.choice(oyuncu_list)
    path = os.path.join(f"./oyuncular/{oyuncu}")
    with open(path, "rb") as doc:
        file = discord.File(doc)
    await ctx.send(file = file)

zengin_list = os.listdir("./zenginler")
@bot.command("zengin")
async def zengin(ctx):
    zengin = random.choice(zengin_list)
    path = os.path.join(f"./zenginler/{zengin}")
    with open(path, "rb") as doc:
        file = discord.File(doc)
    await ctx.send(file = file)

taktikci_list = os.listdir("./taktikciler")
@bot.command("taktikci")
async def taktikci(ctx):
    taktikci = random.choice(taktikci_list)
    path = os.path.join(f"./taktikciler/{taktikci}")
    with open(path, "rb") as doc:
        file = discord.File(doc)
    await ctx.send(file = file)





def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

url = "https://api.currencyapi.com/v3/latest"
headers = {
    'apikey': CURRENCY_TOKEN
}

@bot.command("dolar")
async def dolar(ctx):
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    data_try = data["data"]["TRY"]["value"]
    await ctx.send(f"dolar: {data_try}")


bot.run(TOKEN)