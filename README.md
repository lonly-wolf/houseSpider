## About Spider

### EarthQuackSpider

#### 简介

该spider将会从中国地震台官网 http://news.ceic.ac.cn/ 拉取最新的地震信息

#### 用法

切换至__init__.py 所在的目录下，然后执行以下命令：
    scrapy crawl ceic -o ceic.json
爬取结果将被保存在 ceic.json 文件中

### NewHouseSpider

#### 简介

该spider将会从链家官网拉取北京地区的新楼盘信息 http://bj.fang.lianjia.com/loupan/

#### 用法

切换至__init__.py 所在的目录下，然后执行以下命令：
    scrapy crawl newHouse -o newhouse.json
爬取结果将被保存在 ceic.json 文件中

### OldHouseSpider

#### 简介

该spider将会从链家官网拉取北京地区的二手房信息 https://bj.lianjia.com/ershoufang/

#### 用法

切换至__init__.py 所在的目录下，然后执行以下命令：
    scrapy crawl newHouse -o newhouse.json

爬取结果将被保存在 ceic.json 文件中


### 参考链接

* https://doc.scrapy.org/en/latest/index.html
* http://scrapy-chs.readthedocs.io/zh_CN/1.0/topics/items.html
* https://www.ctolib.com/topics-118320.html#articleHeader0
* https://ask.hellobi.com/blog/pythoncrawl/6196





























## 基于链家网站数据的房价提取分析

### 新房数据抓取规则

楼盘名称： div[@class='col-1']/h2/a/text()
楼盘地址： div[@class='where']/span/text()
建筑面积： div[@class='area']/span/text()
平均价格： div[@class='average']/span/text()
链接网站： div[@class='col-1']/h2/a/@href

下一页： <a href="/loupan/pg2/" data-page="2">下一页</a>

notes: 若存在多重嵌套情况，则可以按照以上模式继续嵌套，例如： div[@class='communityName']/a[@class='info']/text()

###二手房数据抓取规则

小区名称： div[@class='houseInfo']/a/text()   
小区地址： div[@class='positionInfo']/a/text()
平均价格： div[@class='unitPrice']/span/text()
链接网站： div[@class='title']/a/@href

下一页： 


## 测试网站

* http://www.jianshu.com/p/884cf64c1bb1
* https://www.ctolib.com/topics-118320.html#articleHeader0
* https://bj.lianjia.com/ershoufang/
* http://www.cnblogs.com/gcm688/p/6497536.html
* https://zhuanlan.zhihu.com/p/24659468
* http://blog.csdn.net/qiqiyingse/article/details/68944885
