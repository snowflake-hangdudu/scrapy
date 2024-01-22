import requests
import re
from lxml import etree

#提取文字的方法
def extract_text_from_html(html_string):
    tree = etree.HTML(html_string)
    text = tree.xpath('string()')
    return text


def extract_text_from_html(html_string):
    tree = etree.HTML(html_string)
    text = tree.xpath('string()')
    return text

#hot_search列表
hot_search_list = ['深圳大学','深大']

#baseurl
base_url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E6%B7%B1%E5%9C%B3%E5%A4%A7%E5%AD%A6&page_type=searchall'
#第几页
# url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E6%B7%B1%E5%9C%B3%E5%A4%A7%E5%AD%A6&page_type=searchall&page=4

# response = requests.get(base_url)
# json_data = response.json()
# print(json_data)
# print(json_data['data']['cards'],'我是列表')

# for i in json_data['data']['cards']:
#     if(i['card_type'] == 11):
#         continue
#     else:
#         # i['mblog']['text']
#         # print(i)
#         print(extract_text_from_html(i['mblog']['text']))

#前五页的内容
for i in range(1,6):
    if(i==1):
        url = base_url
        print(url)
        response = requests.get(url)
        json_data = response.json()
        for i in json_data['data']['cards']:
            if(i['card_type'] == 11):
                continue
            elif(i['card_type'] == 9):
                #内容
                print(extract_text_from_html(i['mblog']['text']))
                #标题
                print(extract_text_from_html(i['mblog']['text']))
                #链接
                print(i['scheme'])
                print('---------------------------------------------------------------\n')
    else:
        url = base_url + f'&page={i}'
        print(url)
        response = requests.get(url)
        json_data = response.json()
        for i in json_data['data']['cards']:
            if(i['card_type'] == 9):
            #内容
              print(extract_text_from_html(i['card_group'][0]['mblog']['text']))
              #标题
              print(extract_text_from_html(i['card_group'][0]['mblog']['text']))
              # 链接
              print(i['scheme'])
              print('---------------------------------------------------------------\n')
            