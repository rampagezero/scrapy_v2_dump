# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TokpedOsaItem(scrapy.Item):
    name=scrapy.Field()
    url=scrapy.Field()
    count_sold=scrapy.Field()
    stock=scrapy.Field()
    rating=scrapy.Field()
    review=scrapy.Field()
    price=scrapy.Field()
    original_price=scrapy.Field()
    shop_name=scrapy.Field()
    category=scrapy.Field()
    pass
