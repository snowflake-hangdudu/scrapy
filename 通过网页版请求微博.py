# import urllib.request


# #网页版
# # https://m.weibo.cn/u/6239620007?t=0&luicode=10000011&lfid=231583

# url = "https://s.weibo.com/weibo?q=%E6%B7%B1%E5%9C%B3%E5%A4%A7%E5%AD%A6"
# # headers = {
# #     "Accept": "application/json, text/plain, */*",
# #     "Accept-Encoding": "gzip, deflate, br",
# #     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
# #     "Cookie": "_T_WM=61069286102; XSRF-TOKEN=a9377e; WEIBOCN_FROM=1110006030; MLOGIN=0; mweibo_short_token=0199d307da; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D231583%26fid%3D1005056239620007%26uicode%3D10000011",
# #     "Mweibo-Pwa": "1",
# #     "Referer": "https://m.weibo.cn/u/6239620007?t=0&luicode=10000011&lfid=231583",
# #     "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
# #     "Sec-Ch-Ua-Mobile": "?0",
# #     "Sec-Ch-Ua-Platform": "\"Windows\"",
# #     "Sec-Fetch-Dest": "empty",
# #     "Sec-Fetch-Mode": "cors",
# #     "Sec-Fetch-Site": "same-origin",
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
# #     "X-Requested-With": "XMLHttpRequest",
# #     "X-Xsrf-Token": "a9377e"
# # }

# # request = urllib.request.Request(url=url,headers=headers)
# # response = urllib.request.urlopen(request)

import requests

# 发送GET请求
response = requests.get('https://m.weibo.cn/api/container/getIndex?t=0&luicode=10000011&lfid=231583&type=uid&value=6239620007&containerid=1076036239620007')

# 深大大学官博的信息接口
# https://m.weibo.cn/api/container/getIndex?t=0&luicode=10000011&lfid=231583&type=uid&value=6239620007&containerid=1076036239620007
#具体链接怎么拼再研究


#深圳大学搜索的接口
# https://m.weibo.cn/api/container/getIndex?containerid=231583&page_type=searchall

#拿到response,需要解析内容
text = "\u90a3\u4e9b\u672c\u5730\u4eba\u90fd\u4e0d\u77e5\u9053\u7684\u672c\u5730\u7279\u4ea7"
decoded_text = text.encode('utf-8').decode('unicode_escape')

print(decoded_text)





# 获取响应内容
data = response.text

# 打印响应内容
print(data)