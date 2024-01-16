from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import json


driver = webdriver.Chrome()
   #访问网站
url = 'https://weibo.com/login.php'
driver.get(url)

#获取网页源码
content = driver.page_source
time.sleep(5)
#输入账号
zhanghao = driver.find_element(By.XPATH,'//*[@id="loginname"]')
zhanghao.send_keys('15551359775')
time.sleep(1)

#输入密码
password = driver.find_element(By.XPATH,'//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
password.send_keys('hangdudu')

#点击登录
login= driver.find_element(By.XPATH,'//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
login.click()
time.sleep(6)

dictCookie = driver.get_cookies() #获取list的cookies
jsonCookie = json.dumps(dictCookie) #转换成json格式
print(jsonCookie,'cookies')
with open('cookies.txt','w') as fp:
 fp.write(jsonCookie)

#点击验证码输入框
code = driver.find_element(By.XPATH,'//*[@id="pl_login_form"]/div/div[3]/div[3]/div/input')

codeImg = driver.find_element(By.XPATH,'//*[@id="pl_login_form"]/div/div[3]/div[3]/a/img')
print(codeImg.get_attribute("src"))


time.sleep(5)
#手动输入验证码的时间
           

login.click()


# 打印网页源码
print(content,'我是网页源码')