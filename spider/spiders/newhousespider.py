#!/usr/bin/env python3

'''
file name: newhousespider.py
this is a spider
mainly to grab lianjia's new house data
'''
import scrapy
from houseitem import NewHouseItem

class NewHouseSpider(scrapy.Spider):
    name = "newHouse"
    headers = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Host':'bj.fang.lianjia.com',
        'Referer':'http://bj.fang.lianjia.com/loupan/',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
    }
    meta = {
        'dont_redirect' : True,
        'handle_httpstatus_list' : [200, 301, 302, 304, 400, 404]
    }

    def start_requests(self):
        urls = ['http://bj.fang.lianjia.com/loupan/']

        for url in urls:
            print("scan current url:{}".format(url))
            yield scrapy.Request(url = url, headers = self.headers, callback = self.parse, meta = self.meta)

    def parse(self, response):
        print("...............................................................................................................................................")
        houseListOnePage = response.xpath('//div[@class="list-wrap"]/ul[@class="house-lst"]/li[@data-index="0"]')
        for href in houseListOnePage:
            print("********************************************************************************************************")
            item = NewHouseItem()
            item['houseName'] = href.xpath('div[@class="info-panel"]/div[@class="col-1"]/h2/a/text()').extract_first()
            item['houseAddr'] = href.xpath('div[@class="info-panel"]/div[@class="col-1"]/div[@class="where"]/span/text()').extract_first()
            item['houseArea'] = href.xpath('div[@class="info-panel"]/div[@class="col-1"]/div[@class="area"]/span/text()').extract_first()
            item['averagePrice'] = href.xpath('div[@class="info-panel"]/div[@class="col-2"]/div[@class="price"]/div[@class="average"]/span/text()').extract_first()
            item['houseWeb'] = 'http://bj.fang.lianjia.com' + href.xpath('div[@class="info-panel"]/div[@class="col-1"]/h2/a/@href').extract_first()
            yield item

        currentPage = response.xpath("//div[@class='page-box house-lst-page-box']/@page-data").extract_first().split(',')[1].split(':')[1].split('}')[0]
        nextPage = int(currentPage) + 1
        totalPage = int(response.xpath("//div[@class='page-box house-lst-page-box']/@page-data").extract_first().split(',')[0].split(':')[1])
        print("currentPage:{}".format(currentPage))
        print("nextPage:{}".format(nextPage))
        print("totalPage:{}".format(totalPage))
        if nextPage <= totalPage:
            nextUrl = 'http://bj.fang.lianjia.com/loupan/pg{}/'.format(nextPage)
            print("nextUrl:{}".format(nextUrl))
            yield scrapy.Request(url = nextUrl, headers = self.headers, callback = self.parse, meta = self.meta)

if __name__ ==  '__main__':
    print("this is a newhousespider")
