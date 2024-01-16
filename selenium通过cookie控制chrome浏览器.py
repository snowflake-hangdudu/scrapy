from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import json
import os
import requests
# selenium语法全部改变，需重新查找资料

driver = webdriver.Chrome()

#浏览器初始化,打开微博登录页面
def init_browser():
   driver.maximize_window()
   driver.get('https://weibo.com/login.php')
   return driver


# # 读取cookies,登录微博
# def login_weibo():
#    #打开微博页面
#    init_browser()
#    cookies = read_cookies()
#    for cookie in cookies:
#       driver.add_cookie(cookie)
#    time.sleep(10)
#    driver.refresh()
#    time.sleep(1000)
   


def get_cookies():
   #访问网站
   url = 'https://weibo.com/login.php'
   driver.get(url)
   # 60s时间用来登录的
   time.sleep(30)
   Cookies = driver.get_cookies() #获取list的cookies
   jsonCookie = json.dumps(Cookies) #转换成json格式
   print(jsonCookie,'cookies')
   with open('cookies.txt','w') as fp:
    fp.write(jsonCookie)
   print("cookies已重新写入")


def read_cookies():
    #检查文件是否存在
    files = os.path.exists('./cookies.txt')
    if files:
      with open('cookies.txt','r',encoding='utf-8') as fp:
        Cookies = json.load(fp)
        print(Cookies,'cookies已读取')
      cookies = []
      for cookie in Cookies:
          print(cookie,'我是cookie')
          cookie_dict = {
          'domain':'.weibo.com',
          'name':cookie.get("name"),
          'value':cookie.get("value"),
          'expires':'',
          'path':'/',
          'httpOnly':False,
          'HostOnly':False,
          'Secure':False
        }
          cookies.append(cookie_dict)
      return cookies
    else:
      return False
def check_cookie():
   cookies = read_cookies()
   s = requests.Session()
   for cookie in cookies:
      s.cookies.set(cookie['name'],cookie['value'])
   response = s.get('https://weibo.com/u/6239620007')
   response.encoding = response.apparent_encoding
   html_t = response.text
   print(html_t,'我是html_t')
   #检查页面是否包含微博用户名
   if 'hangduduS' in html_t:
      print('登录成功')
      return True
   else:
      print('登录失败')
      return False


if __name__ == '__main__':
   #查看本地是否有cookie
   cookies = read_cookies()
   if cookies:
      #检测cookies的有效性
      res = check_cookie()
      #如果cookie无效
      if res == False:
         #扫码登录微博
         driver = init_browser()
         #获取cookie
         get_cookies()
      else:
         print('cookie有效')
   else:
      #扫码登录微博
      driver = init_browser()
      #获取cookie
      get_cookies()

# login_weibo()





