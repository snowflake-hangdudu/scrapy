import pymysql

# MySQL数据库的主机、端口、用户名、密码、数据库名称和编码
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'hangdudu'
MYSQL_DBNAME = 'hangdudu'
MYSQL_CHARSET = 'utf8'

# 连接到MySQL数据库
try:
    mysql_conn = pymysql.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DBNAME,
        charset=MYSQL_CHARSET
    )
    print("成功连接到MySQL数据库")
except Exception as e:
    print("无法连接到MySQL数据库:", e)

# 添加数据到MySQL数据库
try:
    with mysql_conn.cursor() as cursor:
        sql = "INSERT INTO hangdudu (name) VALUES (%s)"
        cursor.execute(sql, ("hangdudu",))
        mysql_conn.commit()
    print("已在MySQL数据库中添加数据：name:hangdudu")
except Exception as e:
    print("无法添加数据到MySQL数据库:", e)
finally:
    mysql_conn.close()