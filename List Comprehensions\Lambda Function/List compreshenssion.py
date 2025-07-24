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
matched = [w for w in words if re.fullmatch(r'(.).*\1', w)]
print(matched)
