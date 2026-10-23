import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event  # bot belirli bir olay gerçekleştiğinde tetiklensin.
async def on_ready():  # bot başarılı bir şekilde Discord'a bağlandığında tetiklenir
    print(f'{bot.user} olarak giriş yaptık')
    kanal = bot.get_channel(1555652296661143614)

    if kanal:
        await kanal.send("""
🤖 **BOT ÇEVRİMİÇİ!**

📜 **KOMUT LİSTESİ**

❓ `$yardim` - Komut listesini açar
♻️ `$geri_donusum` - Geri dönüşüm malzemeleri
🟢 `$cam` - Cam kutusunun rengi
🔵 `$kagit` - Kağıt kutusunun rengi
🟡 `$plastik` - Plastik kutusunun rengi
🔴 `$pil` - Pil kutusunun rengi
ℹ️ `$bilgi` - Geri dönüşüm hakkında bilgi
🏠 `$neyapmaliyiz` - Evde geri dönüşüm
""")

@bot.command()
async def geri_donusum(ctx):
    await ctx.send("Geri dönüştürülebilir malzemeler: Cam, kağıt, plastik ve metal. Unutmayın, geri dönüşüm önemlidir!"),

@bot.command()
async def cam(ctx):
    await ctx.send("Cam geri dönüşüm kutusunun rengi : Yeşil")

@bot.command()
async def kagit(ctx):
    await ctx.send("Kağıt geri dönüşüm kutusunun rengi : Mavi")

@bot.command()
async def plastik(ctx):
    await ctx.send("Plastik geri dönüşüm kutusunun rengi : Sarı")

@bot.command()
async def pil(ctx):
    await ctx.send("Pil geri dönüşüm kutusunun rengi : Kırmızı")

@bot.command()
async def bilgi(ctx):
    await ctx.send("Geri dönüşüm; kullanım dışı kalan kağıt, cam, plastik ve metal gibi atık malzemelerin çeşitli fiziksel veya kimyasal işlemlerden geçirilerek ham maddeye dönüştürülmesi ve yeniden üretim sürecine kazandırılmasıdır")

@bot.command()
async def neyapmaliyiz(ctx):
    await ctx.send("Evde geri dönüşüm yapmak için cam, kağıt, plastik ve pil türü atıkları her tür için farklı çöp poşetlerinde ayırmalı; sonra poşet dolunca o poşetteki türü o türün geri dönüşüm kutusuna(rengiyle ayrıştırabilirsiniz) atmalıyız.")

@bot.command()
async def yardim(ctx):
    await ctx.send("""
🤖 **BOT ÇEVRİMİÇİ!**

📜 **KOMUT LİSTESİ**

❓ `$yardim` - Komut listesini açar
♻️ `$geri_donusum` - Geri dönüşüm malzemeleri
🟢 `$cam` - Cam kutusunun rengi
🔵 `$kagit` - Kağıt kutusunun rengi
🟡 `$plastik` - Plastik kutusunun rengi
🔴 `$pil` - Pil kutusunun rengi
ℹ️ `$bilgi` - Geri dönüşüm hakkında bilgi
🏠 `$neyapmaliyiz` - Evde geri dönüşüm
""")

# Bu özellik, botun kendisine gönderilen komutları tanıması için bir ön ek tanımlar.
# $ işareti komut ön eki olarak belirlenmiştir. Yani bot sadece $ ile başlayan komutları algılar.


bot.run("")
