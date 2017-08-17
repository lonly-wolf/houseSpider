#!/usr/bin/env python3

'''
file name: oldhousespider.py
this is a spider
mainly to grab lianjia's old house data
'''
import scrapy
from houseitem import OldHouseItem

class OldHouseSpider(scrapy.Spider):
    name = "oldHouse"

    def start_requests(self):
        urls = [
        'https://bj.lianjia.com/ershoufang/pg1/'
        ]
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        for href in response.xpath("//div[@class='info clear']"):
            item = NewHouseItem()
            item['houseName'] = href.xpath("div[@class='address']/div[@class='houseinfo']/a/text()").extract_first()
            item['houseAddr'] = href.xpath("div[@class='flood']/div[@class='positionInfo']/a/text()").extract_first()
            item['averagePrice'] = href.xpath("div[@class='priceInfo']/div[@class='unitPrice']/span/text()").extract_first()
            item['houseWeb'] = href.xpath("div[@class='title']/a/@href").extract_first()
            yield item

        currentPage = response.xpath("//div[@class='page-box house-lst-page-box']/@page-data").extract_first().split(',')[1].split(':')[1]
        nextPage = int(currentPage[0]) + 1
        totalPage = int(response.xpath("//div[@class='page-box house-lst-page-box']/@page-data").extract_first().split(',')[0].split(':')[1])
        if nextPage <= totalPage:
            nextUrls = 'pg%s/' % nextPage
            nextUrls = response.urljoin(nextUrls)
            yield scrapy.Request(nextUrls, callback = self.parse)

if __name__ ==  '__main__':

    print("current scrapy version")
