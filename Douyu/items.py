# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 图片链接
    image_link = scrapy.Field()

    # 图片保存路径
    image_path = scrapy.Field()

    # 主播名
    nick_name = scrapy.Field()

    # 房间号
    room_id = scrapy.Field()

    # 所在城市
    city = scrapy.Field()

    # 数据源
    source = scrapy.Field()

