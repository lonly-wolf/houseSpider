#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
file name: dataformator.py
description: this script  is used to convert data format to anothrer format which supported by baidu hotmap
source data is come from spider
'''

import json
from urllib2 import urlopen
from urllib2 import quote

def load(filePath):
    try:
        with open(filePath) as jsonFile:
            data = json.load(jsonFile)
            return data
    except:
        print("open file failed, please recheck file path or permission!")

def getPosition(address):
    url = 'http://api.map.baidu.com/cloudgc/v1?'
    ak = '8ZxthUScD9ktwOwjNRwg4xN6BCTm6qeC'
    address = quote(address)
    url = url + 'ak=' + ak + '&address=' + address
    requestData = urlopen(url)
    print(requestData)
    requestData = requestData.read().decode("UTF-8")
    temp = json.load(requestData)
    return temp

if __name__ ==  '__main__':

    testPath = 'D:/web/newhouse.json'
    result = load(testPath)

    for i in result:
        strData = i['houseAddr']
        print(strData)
        getPosition('KFC')
        exit(0)

print("********************************************************")