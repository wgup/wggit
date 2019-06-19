# coding: utf-8

#1.将目标网站上的页面抓取下来
#2.将抓取下来的数据根据一定的规则进行提取

import requests
import json
from lxml import etree
#1.将目标网站上的页面抓取下来
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Referer':'https://www.douban.com/',
}
url='https://movie.douban.com/'
response=requests.get(url, headers=headers)
# print response.encoding
# html= etree.parse(response.text, etree.HTMLParser())
html=etree.HTML(response.text)

ul=html.xpath("//ul[@class='ui-slide-content']")
print(ul)
# for li in ul:
#     title= li.xpath('li/@data-title')
#     print(title)

movies=[]
for li in ul:
    title=li.xpath('li/@data-title')
    score=li.xpath('li/@data-rate')
    duration=li.xpath('li/@data-duration')
    region=li.xpath('li/@data-region')
    director=li.xpath('li/@data-director')
    actors=li.xpath('li/@data-actors')
    thumbnail=li.xpath('.//img/@src')
    # print(title, score, duration, region, director, actors, thumbnail)
    movie={
        'title':title,
        'score':score,
        'duration':duration,
        'region':region,
        'director':director,
        'actors':actors,
        'thumbnail':thumbnail
    }
    movies.append(movie)
print (json.dumps(movies, ensure_ascii=False))
# print type(json.dumps(movies))
