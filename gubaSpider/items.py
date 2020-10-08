# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GubaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    read_number=scrapy.Field()
    command_number=scrapy.Field()
    title=scrapy.Field()
    title_url=scrapy.Field()
    author=scrapy.Field()
    author_url=scrapy.Field()
    date=scrapy.Field()

class ContentspiderItem(scrapy.Item):

    title_url=scrapy.Field()
    content=scrapy.Field()

class AuthorspiderItem(scrapy.Item):

    author_url=scrapy.Field()
    following_number=scrapy.Field()
    follower_number=scrapy.Field()
