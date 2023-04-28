import os
import discord
import asyncio
import random
import re

activity = discord.Game(name="bit.ly/stytsko")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(command_prefix=">", activity=activity, intents=intents)

counter = 0

def escape_string(word):
    # escape double quotes in the word with a backslash
    return word.replace('"', r'\"')


@client.event
async def on_message(message):
    global counter

    server_id = message.guild.id
    directory = "databases"
    filename = f"{directory}/wordsdb_{server_id}.txt"
    
    # create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # store each word in a words database for this server
    if message.author != client.user:
        words = message.content.split()
        with open(filename, "a") as f:
            for word in words:
                if word != "<@1072605270066344016>" and message.author.id != "1072605270066344016":
                    escaped_word = escape_string(word)
                    f.write(f'{escaped_word} ')

    # increment the counter
    counter += 1

    # send an expression when the counter reaches 30
    if counter >= 30:
        with open(filename, "r") as f:
            words_str = f.read()
            words = words_str.split()
            if len(words) > 0:
                num_words = min(random.randint(1, 5), len(words))
                expression = " ".join(random.sample(words, num_words))
                await message.channel.send(expression)
            counter = 0

    # respond to mention
    if client.user in message.mentions:
        with open(filename, "r") as f:
            words_str = f.read()
            words = words_str.split()
            if len(words) > 0:
                num_words = min(random.randint(1, 5), len(words))
                expression = " ".join(random.sample(words, num_words))
                await message.channel.send(expression)

            counter = 0

client.run("ВАШ ТОКЕН ТУТ")



