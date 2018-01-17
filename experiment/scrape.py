import json

import requests
from bs4 import BeautifulSoup


STACK_OVERFLOW_URL = "https://stackoverflow.com/questions/tagged/python?sort=votes&pageSize=15"

PARSER = 'html.parser'



result = requests.get(STACK_OVERFLOW_URL)

so_content = result.content

# BeautifulSoup object
# could also accept a filename instead of string
soup = BeautifulSoup(so_content, PARSER)

samples = soup.find_all("a", "question-hyperlink")

# print(samples[0].text)

for s in range(len(samples)):
    print(samples[s].text)

# s
# titles_JSON = json.load(samples)
#
# print(titles_JSON)
