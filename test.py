from bs4 import BeautifulSoup
import urllib.request
from dotenv import load_dotenv
import os

load_dotenv()

suumo_url = os.getenv('SUUMO_URL')

res = urllib.request.urlopen(suumo_url)

name = ''
fee = ''
address = ''

soup = BeautifulSoup(res.read(), 'html.parser')
contents = soup.find_all('div', class_='property')

for content in contents:

    if content.select('a.js-cassetLinkHref'):
        name = content.select('a.js-cassetLinkHref')[0].get_text()

    if content.select('div.detailbox-property-point'):
        fee = content.select('div.detailbox-property-point')[0].get_text()
    
    if content.select('td.detailbox-property-col'):
        address = content.select('td.detailbox-property-col')[4].get_text().strip()


    print("場所" + address + " " + name + "  家賃" + fee)
