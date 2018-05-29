# -*- coding: utf-8 -*-
import json
import scrapy
from Douyu.items import DouyuItem

class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']

    offset = 0

    # 请求url
    base_url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    start_urls = [base_url + str(offset)]

    def parse(self, response):

        # 手机端斗鱼返回的是json格式的数据，所有数据都在data中
        # 直接从请求响应体中获取数据
        node_list = json.loads(response.body)['data']

        # 如果拿不到数据，说明已经爬取完所有翻页
        if not node_list:
            return

        # 对具体数据进行解析
        for node in node_list:

            # 数据保存
            item = DouyuItem()
            item['image_link'] = node['vertical_src']
            item['nick_name'] = node['nickname']
            item['room_id'] = node['room_id']
            item['city'] = node['anchor_city']

            yield item

        # 实现翻页
        self.offset += 20
        yield scrapy.Request(self.base_url + str(self.offset), callback=self.parse)

