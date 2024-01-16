import urllib.request

#网页版
# https://m.weibo.cn/u/6239620007?t=0&luicode=10000011&lfid=231583

url = "https://s.weibo.com/weibo?q=%E6%B7%B1%E5%9C%B3%E5%A4%A7%E5%AD%A6"
header = {
 'cookie':'WBtopGlobal_register_version=2024011516; _s_tentry=-; Apache=4317332444177.7905.1705372335378; SINAGLOBAL=4317332444177.7905.1705372335378; ULV=1705372335394:1:1:1:4317332444177.7905.1705372335378:; PC_TOKEN=3c41ee0437; login_sid_t=2a0544e5c414219610dff31b923d947f; cross_origin_proto=SSL; ALF=1707985902; SUB=_2A25Iok6_DeRhGeBN7lEX-S_KyDiIHXVr3s53rDV8PUJbkNAGLW3WkW1NRHRtEkYpaYmrEhUzGMiP9U_akF3HVv7H; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whn8sapqyT0O96fNQxfF21l5JpX5KzhUgL.Foq0SKec1K2ce0B2dJLoI7LQqg4r9GH.UHet',
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

request = urllib.request.Request(url=url,headers=header)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(content)