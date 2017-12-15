# will need parsers at some point

import requests
from bs4 import BeautifulSoup


STACK_OVERFLOW_URL = "https://stackoverflow.com/questions/tagged/python?sort=votes&pageSize=15"



result = requests.get(STACK_OVERFLOW_URL)

so_content = result.content

soup = BeautifulSoup(so_content)

samples = soup.find_all("a", "question-hyperlink")

for s in range(len(samples)):
    print(s)
    print(samples[s])
