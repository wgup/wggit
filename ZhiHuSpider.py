#!/usr/bin/env python
# coding: utf-8

import requests
import json

from lxml import etree

site_headers = {
    # 'Referer':'https://www.zhihu.com/hot',

    'cookie': '_zap=eab19f61-75d7-48c6-8ba0-c892a041eb4e; _xsrf=jS3x4ZSVimYzAVTOshXNfn9eqMGERfxv; d_c0="AOBvoDM_mg-PTt14Nu40SwIgtw5RiveryEA=|1560829370"; q_c1=6464182b4c4f4101a618596d3c717fce|1560829417000|1560829417000; tst=h; tshl=; tgw_l7_route=80f350dcd7c650b07bd7b485fcab5bf7; capsion_ticket="2|1:0|10:1560932423|14:capsion_ticket|44:NzBmYTJkNzBlOGM4NDQ4NGFhMDcyNzBjOGVlZWVjMTY=|091cd4afa5207b0c0b39b25889dd95dad185c2446b2a7da32d2a9b162eb8a8bd"; z_c0="2|1:0|10:1560932467|4:z_c0|92:Mi4xemtyTEFnQUFBQUFBNEctZ016LWFEeVlBQUFCZ0FsVk5jejczWFFDWVZGYTZ2bkdMMW9UemVJSGJ3Sm5FUGFHSEJB|17d45bf524fc3e4433bfdaad952e970edafdedc8da8c252da5c3032d3a44f730"',
    # 'cookie': '_zap=eab19f61-75d7-48c6-8ba0-c892a041eb4e; _xsrf=jS3x4ZSVimYzAVTOshXNfn9eqMGERfxv',

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

