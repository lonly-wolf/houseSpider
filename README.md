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
