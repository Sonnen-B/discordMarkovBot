import re
import random
import json

# Read the preprocessed text from a file
with open('C:/Users/grant/OneDrive/Desktop/newdiscordtext2.txt', 'r') as file:
    text = file.read()

# Split text into tokens using regular expressions
tokens = re.findall(r':\w+:|\w+|[.,!?;]', text)  # Corrected pattern

# Filter out tokens that are only numbers
words_to_filter = ["brotatorex", "sonnenblume", "chelitopower", "blingbloing", ".brobafett", "ariellavemir", "pm", "gamespate", "brobafett" "soulfulyin", "highaltitude"]
tokens = [token for token in tokens if not (token.isdigit() or token == ':' or token in words_to_filter)]

# Building the Markov dictionary
markov_dict = {}
for i in range(len(tokens) - 1):
    current_word = tokens[i]
    next_word = tokens[i + 1]

    if current_word not in markov_dict:
        markov_dict[current_word] = []

    markov_dict[current_word].append(next_word)

# Serialize and save the Markov dictionary
with open('markov_dict2.json', 'w') as file:
    json.dump(markov_dict, file)