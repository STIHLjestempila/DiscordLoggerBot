from fileinput import close
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(''):
        print(str(message.content))

        file = open("log.log", "a+")
        file.write(str(message.guild) + ":" + str(message.channel) + ":" + str(message.author) + ":" + str(message.content) + "\n")
        file.close()

        return

client.run('OTg5OTYwMjg4MTcyMzk2NTg0.GHbmGp.qIRce07b6s3ntVJRIE_sNUQW4OmQq1hM07kOVw')