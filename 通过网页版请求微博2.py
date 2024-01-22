import requests
import json
import datetime


#前十条的链接
# https://m.weibo.cn/api/container/getIndex?t=0&luicode=10000011&lfid=231583&type=uid&value=6239620007&containerid=1076036239620007
# https://m.weibo.cn/api/container/getIndex?t=0&luicode=10000011&lfid=231583&type=uid&value=6239620007&containerid=1076036239620007&since_id=4991508688404891
# https://m.weibo.cn/api/container/getIndex?t=0&luicode=10000011&lfid=231583&type=uid&value=6239620007&containerid=1076036239620007&since_id=4990845356873287
# https://m.weibo.cn/api/container/getIndex?t=0&luicode=10000011&lfid=231583&type=uid&value=6239620007&containerid=1076036239620007&since_id=4988535469244999


# 发送GET请求
response = requests.get('https://m.weibo.cn/api/container/getIndex?t=0&luicode=10000011&lfid=231583&type=uid&value=6239620007&containerid=1076036239620007')



# decoded_text = text.encode('utf-8').decode('unicode_escape')
# print(decoded_text)



# 获取响应内容
data = response.text


data = json.loads(data)


#响应总条数
total = data['data']['cardlistInfo']['total']




# 打印ok的值
print(data['data']['cards'][0]['mblog']['text'])
current_datetime = datetime.datetime.now()

# 将日期和时间转换为时间戳
timestamp = current_datetime.timestamp()

print(timestamp)