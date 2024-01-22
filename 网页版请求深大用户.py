import requests
import re
from lxml import etree

#提取文字的方法
def extract_text_from_html(html_string):
    tree = etree.HTML(html_string)
    text = tree.xpath('string()')
    return text

#转换链接的方法 
def mid2url(mid):
   output = re.sub(r'\\', '', mid)
   return output

# 发送GET请求
# response = requests.get('https://m.weibo.cn/api/container/getIndex?t=0&luicode=10000011&lfid=231583&type=uid&value=6239620007&containerid=1076036239620007')
#第一页连接
# https://m.weibo.cn/api/container/getIndex?t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%B7%B1%E5%9C%B3%E5%A4%A7%E5%AD%A6&type=uid&value=6239620007&containerid=1076036239620007
#第二页连接
# https://m.weibo.cn/api/container/getIndex?t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%B7%B1%E5%9C%B3%E5%A4%A7%E5%AD%A6&type=uid&value=6239620007&containerid=1076036239620007&since_id=4991877749410959

# data = response.text
# 解析JSON格式的响应内容
# json_data = response.json()

# 打印深大的属性，总微博数，since_id,自动加载数
# since_id = json_data['data']['cardlistInfo']['since_id']
# total = json_data['data']['cardlistInfo']['total']
# autoLoadMoreIndex = json_data['data']['cardlistInfo']['autoLoadMoreIndex']
# print(json_data['data']['cardlistInfo']['since_id'])
# print(json_data['data']['cardlistInfo']['total'])
# print(json_data['data']['cardlistInfo']['autoLoadMoreIndex'])

# 打印微博内容
# for i in json_data['data']['cards']:
    #标题
    # print()
    #链接
    # print(mid2url(i['scheme']))
    #内容
    # print( extract_text_from_html(i['mblog']['text']))
    #
    

            # item['type'] = 'weibo'
            # item['title'] = i.xpath('./@mid')[0]
            # item['url'] = mid2url(i.xpath('./@mid')[0])
            # item['msg'] = i.xpath('.//p/text()')[0]
            # item['icon_desc'] = ''
            # item['hot_value'] = ''
    



#拿取前5页的内容，自定义页数
for i in range(1, 6):
    if(i == 1):
        url = 'https://m.weibo.cn/api/container/getIndex?t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%B7%B1%E5%9C%B3%E5%A4%A7%E5%AD%A6&type=uid&value=6239620007&containerid=1076036239620007'
    else:
       url = f'https://m.weibo.cn/api/container/getIndex?t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%B7%B1%E5%9C%B3%E5%A4%A7%E5%AD%A6&type=uid&value=6239620007&containerid=1076036239620007&since_id={since_id}'
    response = requests.get(url)
    json_data = response.json()
    since_id = json_data['data']['cardlistInfo']['since_id']
    
    print(i)
    print(since_id)
    for card in json_data['data']['cards']:
        # 类型
        print('weibo')
        # 标题
        print( extract_text_from_html(card['mblog']['text']))
        
        # 链接
        print(mid2url(card['scheme']))
        # 内容
        print( extract_text_from_html(card['mblog']['text']))

        #icon_desc
        print('')
        #hot_value
        print('')


            


