import requests
from bs4 import BeautifulSoup

response = requests.get('https://mobalytics.gg/blog/best-tft-comps/')

content = response.content

soup = BeautifulSoup(content, 'html.parser')

img_lazy = soup.find_all('img', attrs={'loading': 'lazy'})

for img in img_lazy:
    if 'Team Comp' in img.get('alt'):
        print(img.get('src'))
