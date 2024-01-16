import chaojiying

# 1. 实例化
cj = chaojiying.Chaojiying_Client('hangdudu', 'hangdudu', '957120')  #这个看chaojiying.py文件
# 2. 调用识别方法
im = open('a.jpg', 'rb').read()    #使用时注意路径
print(cj.PostPic(im, 1902)['pic_str'])