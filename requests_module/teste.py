import requests
from bs4 import BeautifulSoup

response = requests.get('https://app.mobalytics.gg/tft/comps-guide/pool-party-2F2jPIhEzzCazoFpolqNPaWdgja')

content = response.content

soup = BeautifulSoup(content, 'html.parser')

print(soup.prettify())

print('================================================================')

respII = soup.find_all('div', attrs={'class': 'm-6jx7nj'})

print(respII)

