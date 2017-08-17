#!/usr/bin/env python3

'''
file name: houseitem.py
this is a class about house
mainly to record some house message.
'''
import scrapy

class NewHouseItem(scrapy.Item):
    ''' the item of new house '''
    houseName = scrapy.Field()
    houseAddr = scrapy.Field()
    houseArea = scrapy.Field()
    averagePrice = scrapy.Field()
    houseWeb = scrapy.Field()

class OldHouseItem(scrapy.Item):
    ''' the item of old house '''
    houseName = scrapy.Field()
    houseAddr = scrapy.Field()
    averagePrice = scrapy.Field()
    houseWeb = scrapy.Field()