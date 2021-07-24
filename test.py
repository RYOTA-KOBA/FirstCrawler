from bs4 import BeautifulSoup
import urllib.request

res = urllib.request.urlopen('https://suumo.jp/chintai/jnc_000061987398/?bc=100246128973')

soup = BeautifulSoup(res.read(), 'html.parser')
contents = soup.find('span', class_='property_view_note-emphasis')

fee = contents.get_text()

print(fee)