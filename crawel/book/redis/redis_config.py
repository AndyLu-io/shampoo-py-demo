import redis
import os

# 全局连接池和 Redis 客户端对象
redis_pool = None
redis_client = None

# 获取 Redis 配置信息，可以通过环境变量设置（适用于不同环境）
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')  # 默认本地
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))    # 默认端口6379
REDIS_DB = int(os.getenv('REDIS_DB', 0))           # 默认数据库0
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None) # 如果需要密码可以配置
REDIS_MAX_CONNECTIONS = int(os.getenv('REDIS_MAX_CONNECTIONS', 10))  # 最大连接数

def initialize_redis():
    """初始化 Redis 连接池和客户端"""
    global redis_pool, redis_client

    # 创建 Redis 连接池（全局）
    try:
        redis_pool = redis.ConnectionPool(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB,
            password=REDIS_PASSWORD,
            max_connections=REDIS_MAX_CONNECTIONS
        )

        # 使用连接池创建 Redis 客户端
        redis_client = redis.StrictRedis(connection_pool=redis_pool)

        # 测试连接
        if redis_client.ping():
            print("成功连接到 Redis!")
        else:
            print("连接 Redis 失败！")

    except redis.exceptions.ConnectionError as e:
        print(f"连接失败: {e}")
        redis_pool = None
        redis_client = None
    except Exception as e:
        print(f"初始化 Redis 失败: {e}")
        redis_pool = None
        redis_client = None

def get_redis_client():
    """返回全局的 Redis 客户端对象"""
    initialize_redis()
    if redis_client is None:
        print("Redis 客户端未初始化")
        return None
    return redis_client

def close_redis():
    """关闭 Redis 连接池"""
    global redis_pool, redis_client
    if redis_pool:
        try:
            redis_pool.disconnect()
            print("Redis 连接池已关闭")
        except redis.exceptions.RedisError as e:
            print(f"关闭 Redis 连接池时发生错误: {e}")
        redis_pool = None
        redis_client = None
    else:
        print("Redis 连接池未初始化或已关闭")

if __name__ == '__main__':
    # 初始化 Redis 连接池
    initialize_redis()

    # 使用全局 Redis 客户端进行操作
    client = get_redis_client()
    if client:
        client.set('key', 'value')
        print(client.get('key'))  # 输出 'value'

    # 关闭 Redis 连接池
    close_redis()
