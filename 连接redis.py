
import redis

# Redis数据库的主机、端口和数据库编号
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0

# 连接到Redis数据库
redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB)

# 检查是否成功连接
if redis_client.ping():
    print("成功连接到Redis数据库")
else:
    print("无法连接到Redis数据库")

# 在Redis数据库中添加数据
redis_client.hset("db", "name", "hangdudu")
print("已在Redis数据库中添加数据：name:hangdudu")