import requests
from lxml import etree
import time,random


def down(url):
    response = requests.get(url,headers=headers).text
    html = etree.HTML(response)
    ls = html.xpath('//ul[@class="clearfix"]/li')
    num=1
    for each in ls:
        detail_url = 'http://pic.netbian.com'+ each.xpath('./a/@href')[0]
        response = requests.get(detail_url,headers=headers).text
        html = etree.HTML(response)
        img_url =  'http://pic.netbian.com'+ html.xpath('//div[@class="photo-pic"]//img/@src')[0]
        response = requests.get(img_url, headers=headers).content
        temp = img_url.split('/')[-1]
        path = './wangzhe/'+temp
        print(f'开始爬取第{num}张')
        with open(path,'wb') as  f:
            f.write(response)
        num+=1
        time.sleep(random.random())

if __name__=='__main__':
    headers = {
        'Referer': 'http://pic.netbian.com/4kmeinv/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    url = 'http://pic.netbian.com/e/search/result/index.php?page=0&searchid=1869'
    # url = 'http://pic.netbian.com/4kmeinv'
    # url = 'http://pic.netbian.com/4kdongman'
    page = 1
    while True:
        print(f'第{page}页爬取中')
        if page==1:
            down(url)
        else:
            url = f'http://pic.netbian.com/e/search/result/index.php?page={page-1}&searchid=1869'
            # url = f'http://pic.netbian.com/4kmeinv/index_{page}.html'
            # url = f'http://pic.netbian.com/4kdongman/index_{page}.html'
            down(url)
        page+=1





