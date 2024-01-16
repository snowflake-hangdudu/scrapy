# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import redis
from hashlib import md5
import pymysql


class HangduduPipeline:

    # 创建一个 Redis 客户端对象,用于与 Redis 服务器进行交互,初始值为 None
    def __init__(self):
        self.redis_conn = None

    #在爬虫启动时调用，用于连接到 Redis 服务器
    def open_spider(self, spider):
        self.redis_conn = redis.Redis(host='127.0.0.1', port=6379, db=0)
                # 检查是否成功连接
        if self.redis_conn.ping():
            print("成功连接到Redis数据库")
        else:
            print("无法连接到Redis数据库")




    def process_item(self, item, spider):
        # print(item,'我是process_item的item')
        m5 = md5()
        m5.update(item['title'].encode('utf-8'))
        #spider.name为集合名称，md5为key,m5.hexdigest()为value
        flag = self.redis_conn.sadd(spider.name + ":md5", m5.hexdigest())
        
        
        if flag:
            return item
        return item
    
    def close_spider(self, spider):
        self.redis_conn.close()


class MysqlPipeline:

    def __init__(self):
        self.connect = None
        self.cursor = None

    def open_spider(self, spider):
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='hangdudu',
            db='hangdudu',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        print(item,'我是mysql的process_item')  # 打印 item 对象
        #创建游标对象
        cursor = self.connect.cursor()
        #定义sql语句
        sql = "insert into hangdudu(url,title,msg,type,icon_desc,hot_value) values (%s,%s,%s,%s,%s,%s)"
        #定义要插入的值
        val = (item['url'], item['title'], item['msg'], item['type'], item['icon_desc'], item['hot_value'])
        print(val,'我是val')
        try:
            cursor.execute(sql, val)  # 执行 SQL 插入语句
            self.connect.commit()  # 提交事务
            print("数据成功插入到 hangdudu 表中")  # 打印成功消息
        except Exception as e:
            self.connect.rollback()  # 回滚事务，撤销之前的操作
            print("数据插入失败:", e)  # 打印失败消息


    def close_spider(self, spider):
        self.connect.close()
        