import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

with open('C:/Users/grant/OneDrive/Desktop/newdiscordtext.txt', 'r', encoding='utf-8') as file:
    text = file.read()

text = text.lower()

tokens = word_tokenize(text)

# Removing non-alphanumeric characters except colons and periods
tokens = [re.sub(r'[^a-zA-Z0-9:.]', '', token) for token in tokens if re.sub(r'[^a-zA-Z0-9:.]', '', token)]

lemmatizer = WordNetLemmatizer()
tokens = [lemmatizer.lemmatize(token) for token in tokens]

preprocessed_text = " ".join(tokens)
print(preprocessed_text)

with open('C:/Users/grant/OneDrive/Desktop/newdiscordtext2.txt', 'w', encoding='utf-8') as file:
    file.write(preprocessed_text)

print("Preprocessed text has been written to preprocessed_output.txt")