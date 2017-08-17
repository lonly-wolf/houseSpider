#!/usr/bin/env python3

'''
file name: houseitem.py
this is a class about earth quack item
mainly to record some house message.
'''
import scrapy

class EarthQuackItem(scrapy.Item):
    ''' the item of new house '''
    rate = scrapy.Field()
    time = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    depth = scrapy.Field()
    position = scrapy.Field()
