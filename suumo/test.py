from bs4 import BeautifulSoup
import urllib.request
from dotenv import load_dotenv
import os
import socket

load_dotenv()

suumo_url = os.getenv('SUUMO_URL')
print(suumo_url)

req = urllib.request.urlopen(suumo_url, timeout=10).read()

name = ''
fee = ''
address = ''

soup = BeautifulSoup(req, 'html.parser')
contents = soup.find_all('div', class_='property')

for content in contents:

    if content.select('a.js-cassetLinkHref'):
        name = content.select('a.js-cassetLinkHref')[0].get_text()

    if content.select('div.detailbox-property-point'):
        fee = content.select('div.detailbox-property-point')[0].get_text()
    
    if content.select('td.detailbox-property-col'):
        address = content.select('td.detailbox-property-col')[4].get_text().strip()


    print("場所" + address + " " + name + "  家賃" + fee)
