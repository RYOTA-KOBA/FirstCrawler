from bs4 import BeautifulSoup
import urllib.request

res = urllib.request.urlopen('https://suumo.jp/jj/chintai/ichiran/FR301FC005/?shkr1=03&shkr3=03&cb=0.0&shkr2=03&smk=&mt=9999999&sc=13103&ar=030&bs=040&shkr4=03&ct=15.0&co=1&co=3&cn=5&ta=13&mb=0&fw2=&et=9999999')

name = ''
fee = ''

soup = BeautifulSoup(res.read(), 'html.parser')
contents = soup.find_all('div', class_='property')

for content in contents:

    if content.select('a.js-cassetLinkHref'):
        name = content.select('a.js-cassetLinkHref')[0].get_text()

    if content.select('div.detailbox-property-point'):
        fee = content.select('div.detailbox-property-point')[0].get_text()

    print(name + ":" + fee)
