import scrapy
from bs4 import BeautifulSoup
import urllib.request
from suumo.items import SuumoItem
from dotenv import load_dotenv
import os

load_dotenv()

suumo_url = os.getenv('SUUMO_URL')


class SuumoSpiderSpider(scrapy.Spider):
    name = 'suumo_spider'
    allowed_domains = ['suumo.jp']
    start_urls = [suumo_url]

    def parse(self, response):
        name = ''
        fee = ''
        address = ''

        res = urllib.request.urlopen(suumo_url)
        soup = BeautifulSoup(res.read(), 'html.parser')
        contents = soup.find_all('div', class_='property')

        for content in contents:

            if content.select('a.js-cassetLinkHref'):
                name = content.select('a.js-cassetLinkHref')[0].get_text()

            if content.select('div.detailbox-property-point'):
                fee = content.select('div.detailbox-property-point')[0].get_text()
            
            if content.select('td.detailbox-property-col'):
                address = content.select('td.detailbox-property-col')[4].get_text().strip()

            yield SuumoItem(
                name=name,
                fee=fee,
                address=address
            )

            # next_page = soup.find('p', {'class': 'pagination-parts'})
            # next_page_link = next_page.a
            # # 最後のページではnext_page_linkは存在しなくなるので、それを条件にyield
            # if 'href' not in next_page_link.attrs:
            #     yield

            # # URLの最後のクエリ(page=2の部分)がページによって違うだけ
            # page_num = 2
            # page_num += 1
            # url = suumo_url + &page=page_num
            
            # # print("場所" + address + " " + name + "  家賃" + fee)

            # print(url)

