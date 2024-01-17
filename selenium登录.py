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
#第一种方法,打开图片,手动输入
imgcode = input('请输入验证码:')
code.send_keys(imgcode)

#第二种办法，使用超级鹰自动解码
# import chaojiying
# # 1. 实例化
# cj = chaojiying.Chaojiying_Client('hangdudu', 'hangdudu', '957120')  #这个看chaojiying.py文件
# # 2. 调用识别方法
# im = open('a.jpg', 'rb').read()    #使用时注意路径
# print(cj.PostPic(im, 1902)['pic_str'])

time.sleep(5)
#手动输入验证码的时间

#再次点击登录
login.click()

#点击短信按钮验证

time.sleep(5)
sms = driver.find_element(By.XPATH,'//*[@id="messageCheck"]')
sms.click()

#点击接收验证码验证

time.sleep(5)
receive = driver.find_element(By.XPATH,'//*[@id="message_sms_login"]')
receive.click()



#第一种办法，手动输入短信验证码
time.sleep(10)
code = input('请输入验证码:')




# 打印网页源码
print(content,'我是网页源码')