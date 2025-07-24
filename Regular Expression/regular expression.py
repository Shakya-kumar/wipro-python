import re

# 1. Check if strings have only octal digits
strings = ['789', '123', '004']
octal_check = [bool(re.fullmatch(r'[0-7]+', s)) for s in strings]
print(octal_check)

# 2. Extract user id, domain name and suffix from email addresses
emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""
matches = re.findall(r'([\w\d]+)@([\w\d]+)\.(\w+)', emails)
print(matches)

# 3. Split irregular sentence into proper words
sentence = """A, very very; irregular_sentence"""
words = re.split(r'[;,_\s]+', sentence)
print(" ".join(words))

# 4. Clean tweet to only contain user message
tweet = """Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej@pxOd cc: @garybernhardt #rstats"""
cleaned = re.sub(r"(RT|cc:?)\s?|@\w+|#\w+|http\S+|[^\w\s]", '', tweet)
print(cleaned.strip())

# Extract all the text portions between the tags from the following HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.html

import requests
import re

r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html_text = r.text
result = re.findall(r'>([^<>]+)<', html_text)
output = [text.strip() for text in result if text.strip()]
print(output)

# Given below list of words, identify the words that begin and end with the same character.

words = ['civic', 'trust', 'widows', '6-M', 'maximum', 'museums', 'aa', 'ras']
same_char_words = [w for w in words if re.fullmatch(r'(.).*\1', w)]
print(same_char_words)
