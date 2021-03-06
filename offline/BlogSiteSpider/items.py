#!/usr/bin/python2.7
#coding=utf-8

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html


from scrapy.item import Item, Field

class SiteLinkItem(Item):
    name = Field()
    url = Field()

class SiteWeightItem(Item):
    url = Field()
    weight = Field()
