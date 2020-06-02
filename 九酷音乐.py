import requests
from lxml import etree
import re
import json


def get_content(url):
    '''
    返回网页内容
    :param url:
    :return:
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        # ,'Referer':'http://www.9ku.com/play/996722.htm'
    }
    response = requests.get(url, headers=headers)
    return response


def get_detail(url):
    html = get_content(url).text
    html = etree.HTML(html)
    # 音乐列表
    ls = html.xpath('//ul[@class="musicList"]/li')
    print(len(ls))
    a=1
    for each in ls:
        # href="/play/1003606.htm"
        href = each.xpath('./a[@class="songName "]/@href')[0]
        name = each.xpath('./a[@class="songName "]/@title')[0]
        pat = re.compile(r'(\d+)')
        # print(href)
        muisc_id = pat.search(href).group(1)
        if muisc_id[0] == '1':
            num = str(int(muisc_id[:4]) + 1)
        else:
            num = str(int(muisc_id[:3]) + 1)
        muisc_url = f'http://www.9ku.com/html/playjs/{num}/{muisc_id}.js'
        music = get_content(muisc_url).text
        pat1=re.compile(r'"wma":"(.*?)","')
        json_data = pat1.search(music).group(1)
        temp = json_data.split('\\')
        muisc_detail_url = ''.join(temp)
        # print(muisc_detail_url)
        music_data=get_content(muisc_detail_url).content
        print("="*10+f'第{a}首下载中'+"="*10)
        a+=1
        with open(f'./music/{name}.mp3','wb')as file:
            file.write(music_data)



if __name__ == "__main__":
    url = 'http://www.9ku.com/'
    get_detail(url)
