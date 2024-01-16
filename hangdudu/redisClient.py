import redis

# 创建了一个 Redis 客户端对象 redis_conn，用于连接到 Redis 服务器。
redis_conn = redis.Redis(host='127.0.0.1', port=6379, db=0)

#百度
# redis_conn：Redis 客户端对象，用于与 Redis 服务器进行交互。
# lpush：Redis 的列表操作命令之一。它将指定的值插入到列表的左侧（头部）。
# 'baidup:start_urls'：表示要操作的 Redis 列表键的名称。在这种情况下，是一个名为 "baidup:start_urls" 的列表键。
# 'https://top.baidu.com/board?tab=realtime'：要推送到 Redis 列表中的值，即起始 URL。
redis_conn.lpush('baidup:start_urls', 'https://top.baidu.com/board?tab=realtime')
