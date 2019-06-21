#!/usr/bin/env python
# coding: utf-8

import requests
import json

from lxml import etree

site_headers = {
    # 'Referer':'https://www.zhihu.com/hot',

    'cookie': '填写登录之后的cookie',
    
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
}

site_url = 'https://www.zhihu.com/hot'

response = requests.get(site_url, headers=site_headers)

# text = response.text

html = etree.HTML(response.text)

# infos = html.xpath("//div[@id='TopstoryContent']/div/div/div[2]//section[@class='HotItem']")
infos = html.xpath("//div[@class='HotItem-content']")

# print(infos)
# print(json.dumps(infos, ensure_ascii=False))

items = []

for info in infos:
    hotitem_title = info.xpath('a/h2/text()')
    hotitem_excerpt = info.xpath('a/p/text()')
    hotitem_metric = info.xpath('div/text()')

    item ={
        'hotTitle': hotitem_title,

        'hotExcerpt': hotitem_excerpt,

        'hotMetric': hotitem_metric
    }

    items.append(item)

# for info in infos:
#     hotitem_title = info.xpath('div[@class="HotItem-content"]/a/@title')
#     hotitem_excerpt = info.xpath('div[@class="HotItem-content"]/a/p/text()')
#     hotitem_metric = info.xpath('div[@class="HotItem-content"]/div/text()')
#
#     item ={
#         'hotTitle': hotitem_title,
#
#         'hotExcerpt': hotitem_excerpt,
#
#         'hotMetric': hotitem_metric
#     }
#
#     items.append(item)

print(json.dumps(items, ensure_ascii=False))

