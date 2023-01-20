# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsAggrItem(scrapy.Item):
    source = scrapy.Field()
    date = scrapy.Field()
    title = scrapy.Field()
    brief = scrapy.Field()
