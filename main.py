import discord
import api_token
import time
import random

client = discord.Client()

tag_kevin = "<@!392197689779027968>"
tag_kit = "<@!696701384916992060>"


@client.event
async def on_ready():
    print("user: ", client.user)
    game = discord.Game("Kit")
    await client.change_presence(status=discord.Status.idle, activity=game)


@client.event
async def on_message(message):

    print(message.author)
    print(message.content)

    if str(message.author) == "kimihakimi#4391":
        if "Kit" in message.content or "kit" in message.content:
            await message.channel.send("%s 走，我們來讓阿飄知道我們多聰明！" % tag_kit)
        elif "上班" in message.content:
            await message.channel.send("%s 翹班！走！" % tag_kevin)
        elif "變了" in message.content or "不愛" in message.content:
            await message.channel.send("飄，你不愛我了嗎？")
        elif "三小" in message.content or "三姣" in message.content or "三洨" in message.content:
            await message.channel.send("%s 怎？" % tag_kevin)
        elif len(set(message.content)) == 1:
            length_chat = len(message.content)

            if length_chat > 80:
                length_chat = 80

            if "！" in message.content or "!" in message.content:
                await message.channel.send("%s %s" % (tag_kevin, "？" * length_chat))
            elif "？" in message.content or "?" in message.content:
                await message.channel.send("%s %s" % (tag_kevin, "！" * length_chat))
            elif "欸" in message.content or "诶" in message.content:
                await message.channel.send("%s %s" % (tag_kevin, "嘿" * length_chat + "？"))
            elif "." in message.content or "。" in message.content or "," in message.content:
                await message.channel.send("%s %s" % (tag_kevin, "點沙小？" * length_chat + "？"))
        else:
            await message.channel.send("%s 笨，玩嗎？" % tag_kevin)

    if str(message.author) == "panjojocom#1878":
        if "空對地支援" in message.content:
            this_message = message.content.split("---")

            if len(this_message) < 3:
                return True

            this_content = this_message[2]
            times = int(this_message[1])

            game = discord.Game("空中支援接近中")
            await client.change_presence(status=discord.Status.idle, activity=game)

            for i in range(times):
                await message.channel.send("%s %s" % (tag_kevin, this_content))

            game = discord.Game("已完成 %d 轟炸" % times)
            await client.change_presence(status=discord.Status.idle, activity=game)

            if random.choice([True, False]):
                await message.channel.send("%s %s" % (tag_kit, this_content))
                game = discord.Game("已完成 %d 轟炸，順手轟炸 kit" % times)
                await client.change_presence(status=discord.Status.idle, activity=game)

            time.sleep(3)

            game = discord.Game("Kit")
            await client.change_presence(status=discord.Status.idle, activity=game)


client.run(api_token.main_key)
