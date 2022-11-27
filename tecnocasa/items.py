# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Tecnocasa(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title = scrapy.Field()
    Address = scrapy.Field()
    Price = scrapy.Field()
    Surface = scrapy.Field()
    Rooms = scrapy.Field()
    Baths = scrapy.Field()
    pass
