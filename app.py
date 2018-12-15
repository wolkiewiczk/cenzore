import discord
import asyncio
from discord.ext import commands
from string_utils import StringUtils
from random import randint


bot = commands.Bot(command_prefix="?")
utils = StringUtils(dict="test.json")


@bot.event
async def on_ready():
    print("Bot succesfully started")


@bot.event
async def on_message(message):

    if message.author.bot or message.content == "":
        return

    list_to_check = message.content.split()
    vulgar = False
    to_send = "**" + message.author.mention + " **powiedział(a):\n"

    for word in list_to_check:
        to_check = utils.refactor(word)
        result = utils.binary_search_by_distance(to_check, utils.dictionaries["dict"], 0)
        if result:
            print("Word %s succesfuly cenzored" % word)
            vulgar = True
            i = randint(0, len(utils.dictionaries["dict"][result]["synonyms"])-1)
            to_send += utils.dictionaries["dict"][result]["synonyms"][i] + " "
        else:
            to_send += word + " "
    if vulgar:
        await bot.delete_message(message)
        await bot.send_message(message.channel, to_send)

bot.run('NTA0Njk0MjY3OTAyNjg5Mjkw.DsYxvg.428e1KTf4DygHQIKmzKIV73CAys')

