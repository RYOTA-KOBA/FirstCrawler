# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SuumoItem(scrapy.Item):
    # define the fields for your item here like:
    rent_fee = scrapy.Field()
    location = scrapy.Field()
    
