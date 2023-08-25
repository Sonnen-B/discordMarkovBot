import discord
import random
import json
from discord.ext import commands

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.messages = True

with open('C:/Users/grant/AppData/Local/Programs/Python/Python311/markov_dict2.json', 'r') as file:
    markov_dict = json.load(file)

def generate_text(markov_dict, seed_word, length):
    generated_text = [seed_word]
    current_word = seed_word

    for _ in range(length - 1):
        if current_word in markov_dict:
            next_word = random.choice(markov_dict[current_word])
            generated_text.append(next_word)
            current_word = next_word
        else:
            break

    return ' '.join(generated_text)

max_word_length = 20

# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.command()
# async def generate(ctx):
#     seed_word = random.choice([word for word in markov_dict.keys() if len(word) <= max_word_length])
#     # seed_word = 'hello'  # Change this to your desired seed word
#     generated_text = generate_text(markov_dict, seed_word, 20)  # Adjust length as needed
#     await ctx.send(generated_text)

# # Load the Markov dictionary from JSON
# with open('C:/Users/grant/AppData/Local/Programs/Python/Python311/markov_dict2.json', 'r') as file:
#     markov_dict = json.load(file)

# Initialize the bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize a message counter
message_counter = 0

# Event handler for when a message is sent
@bot.event
async def on_message(message):
    # Ignore messages from the bot itself to prevent loops
    if message.author == bot.user:
        return

    global message_counter

    # Increment the message counter for every message from other users
    message_counter += 1

    # Respond every 20 messages from other users
    if message_counter >= 10:
        # Choose a random seed word from the Markov dictionary keys
        seed_word = random.choice([word for word in markov_dict.keys() if len(word) <= max_word_length])

        # Generate text using the random seed word
        generated_text = generate_text(markov_dict, seed_word, 20)  # Adjust length as needed
        await message.channel.send(generated_text)

        # Reset the message counter
        message_counter = 0

    # Allow other event handlers to continue processing
    await bot.process_commands(message)

bot.run('MTE0NDQ0ODA0NDY3MTE4OTAyMg.GlefEt.MXEiMnBjaphuL5DSTfpLOUyeg0KekCUYOPN8DE')