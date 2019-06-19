import requests
from lxml import etree

url = 'http://www.ygdy8.com/html/gndy/china/index.html'


def get_movie_info(url):
    html = requests.get(url)
    html.encoding = 'gb2312'
    selector = etree.HTML(html.text)
    infos = selector.xpath('//div[@class="co_content8"]/ul//table')
    for info in infos:
        movie_url = 'http://www.ygdy8.com' + info.xpath('tr[2]/td[2]/b/a[2]/@href')[0]
        movie_name = info.xpath('tr[2]/td[2]/b/a[2]/text()')[0]
        print(movie_url,movie_name)
        get_download(movie_url)

def get_download(url):
    html = requests.get(url)
    html.encoding = 'gb2312'
    selector = etree.HTML(html.text)
    down_url = selector.xpath('//tbody/tr/td/a/text()')[0]
    print(down_url)

if __name__ == '__main__':
    get_movie_info('http://www.ygdy8.com/html/gndy/china/index.html')
