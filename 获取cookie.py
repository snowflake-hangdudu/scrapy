from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json


#初始化浏览器
browser = webdriver.Chrome()
   #访问网站
url = 'https://weibo.com/login.php'
browser.get(url)

# 60s时间用来登录的
time.sleep(30)



dictCookie = browser.get_cookies() #获取list的cookies
jsonCookie = json.dumps(dictCookie) #转换成json格式
print(jsonCookie,'cookies')
with open('cookies.txt','w') as fp:
  fp.write(jsonCookie)

print("已经获取到cookie")
browser.quit()


