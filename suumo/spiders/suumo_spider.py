import scrapy
from bs4 import BeautifulSoup


class SuumoSpiderSpider(scrapy.Spider):
    name = 'suumo_spider'
    allowed_domains = ['suumo.jp']
    start_urls = ['https://suumo.jp/']

    def parse(self, response):
        rent_fee = ''
        location = ''

        soup = bs4.BeautifulSoup(response.body, 'html.parser')
        homes = soup.findAll(
            name = 'div',
            attrs={'class': 'homeContent'}
        )

        for home in homes:

            if home.select('span.property_view_note-emphasis'):
                rent_fee = home.select('span.property_view_note-emphasis').get_text()
                


