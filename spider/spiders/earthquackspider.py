#!/usr/bin/env python3

'''
file name: earthquackspider.py
this script will grab earthquack data from http://news.ceic.ac.cn/
this is a spider
'''
import scrapy
from earthquackitem import EarthQuackItem

class EarthQuackSpider(scrapy.Spider):
    name = "ceic"
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'Hm_lvt_e0025cd5d352165f8a646ccea5beb27d=1502867003,1502867509,1502932505; Hm_lpvt_e0025cd5d352165f8a646ccea5beb27d=1502940925',
        'Host':'news.ceic.ac.cn',
        'Referer':'http://news.ceic.ac.cn/',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
    }
    meta = {
        'dont_redirect' : True,
        'handle_httpstatus_list' : [301, 302, 304, 400, 404]
    }

    def start_requests(self):
        urls = ['http://news.ceic.ac.cn/index.html']

        for url in urls:
            print("scan current url:{}".format(url))
            yield scrapy.Request(url = url, headers = self.headers, callback = self.parse, meta = self.meta)

    def parse(self, response):
        print("*************************************************************************************************************")

        for href in response.xpath('//div[@class="news-content"]/table[@class="news-table"]'):
            print("------------------------------------------------------------------------------------------------------")
            tableList = href.xpath('tr/td[@align="center"]/text()').extract()
            locationList = href.xpath('tr/td[@align="left"]/a/text()').extract()

            index = 0
            for i in locationList:
                item = EarthQuackItem()
                item['rate'] = tableList[index + 0]
                item['time'] = tableList[index + 1]
                item['longitude'] = tableList[index + 2]
                item['latitude'] = tableList[index + 3]
                item['depth'] = tableList[index + 4]
                item['position'] = i
                index += 5
                yield item

if __name__ ==  '__main__':
    print("this is earthquack spider.......")
