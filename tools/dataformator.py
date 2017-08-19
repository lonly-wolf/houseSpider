#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
file name: dataformator.py
description: this script  is used to convert data format to anothrer format which supported by baidu hotmap
source data is come from spider
'''

import json
import os
from urllib2 import urlopen
from urllib2 import quote
import types

saveJsonFormat = { "houseName":"Null", "averagePrice":0, "lng":0, "lat":0, "count":0}

def load(filePath):
    try:
        with open(filePath) as jsonFile:
            data = json.load(jsonFile)
            return data
    except:
        print("open file failed, please recheck file path or permission!")

def getPosition(address):
    ''' return type is str '''
    url = 'http://api.map.baidu.com/cloudgc/v1?'
    ak = '8ZxthUScD9ktwOwjNRwg4xN6BCTm6qeC'
    address = address.encode('utf-8')
    address = quote(address)
    url = url + 'ak=' + ak + '&address=' + address
    requestData = urlopen(url).read()
    return requestData

def toHotMapValue(averagePrice):
    ''' this method mainly to convert  averagePrice to hotMap value'''
    ''' hotMap value range: 0-255'''
    ''' average price range 1000 - 30000'''
    ''' factor  = 1 / ((200000 - 1000) / 255) '''

    factor = 1 / 780.3921
    if averagePrice <= 1000:
        return 0
    elif averagePrice >= 200000:
        return 255
    return factor * averagePrice

if __name__ ==  '__main__':

    scriptDir  = os.path.dirname(__file__)
    scriptPath = scriptDir + '\\' + 'newhouse.json'

    testPath = 'D:/web/newhouse.json'
    result = load(testPath)

    with open(scriptPath, 'w') as output:
        output.write('[' + '\n')
        index = 0
        contentCount = len(result)
        for i in result:
            print("writing  newhouse.json file...........{}".format(index))
            strData = i['houseAddr']
            print(u'%s' % strData)
            posInfo = getPosition(u'%s' % strData)
            houseName = i['houseName']
            houseAveragePrice = i['averagePrice']
            # if type(houseAveragePrice) is types.NoneType:
            #     houseAveragePrice = 0


            posInfo = json.loads(posInfo)
            print(posInfo)
            print("**************************************")
            houseLongitude = posInfo['result'][0]['location']['lng']
            houseLatitude = posInfo['result'][0]['location']['lat']
            if type(houseAveragePrice) is types.NoneType:
                houseWeight = 0
            else:
                houseWeight = toHotMapValue(int(houseAveragePrice))

            saveJsonFormat['houseName'] = houseName.encode('utf-8')
            saveJsonFormat['averagePrice'] = houseAveragePrice
            saveJsonFormat['lng'] = houseLongitude
            saveJsonFormat['lat'] = houseLatitude
            saveJsonFormat['count'] = houseWeight
            print(saveJsonFormat)
            print(type(saveJsonFormat))
            json.dump(saveJsonFormat, output, ensure_ascii = False)
            if  index + 1 < contentCount:
                output.write(',')
            index += 1
            output.write('\n')
        output.write(']' + '\n')

print("json file write successfully!")
print("***************************************************************************")