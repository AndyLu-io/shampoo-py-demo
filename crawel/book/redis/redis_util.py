from crawel.book import redis
from redis_config import get_redis_client, close_redis

class RedisUtil:
    @staticmethod
    # 设置键值
    def set_value(key, value, ex=None):
        """
        设置键值对，如果 ex 参数不为 None，则设置过期时间（单位：秒）
        """
        redis_client = get_redis_client()
        try:
            if ex:
                redis_client.setex(key, ex, value)  # 设置过期时间
            else:
                redis_client.set(key, value)  # 不设置过期时间
            print(f"键 {key} 设置成功")
        except redis.exceptions.RedisError as e:
            print(f"设置键 {key} 失败: {e}")

    @staticmethod
    # 获取键值
    def get_value(key):
        """
        获取指定键的值
        """
        redis_client = get_redis_client()
        try:
            value = redis_client.get(key)
            if value is None:
                print(f"键 {key} 不存在")
            else:
                print(f"键 {key} 的值是: {value.decode('utf-8')}")
            return value
        except redis.exceptions.RedisError as e:
            print(f"获取键 {key} 失败: {e}")
            return None

    @staticmethod
    # 删除键
    def delete_key(key):
        """
        删除指定键
        """
        redis_client = get_redis_client()
        try:
            redis_client.delete(key)
            print(f"键 {key} 删除成功")
        except redis.exceptions.RedisError as e:
            print(f"删除键 {key} 失败: {e}")

    @staticmethod
    # 设置哈希表中的字段
    def set_hash_field(hash_name, field, value):
        """
        设置哈希表中的字段
        """
        redis_client = get_redis_client()
        try:
            redis_client.hset(hash_name, field, value)
            print(f"哈希 {hash_name} 中的字段 {field} 设置成功")
        except redis.exceptions.RedisError as e:
            print(f"设置哈希 {hash_name} 中字段 {field} 失败: {e}")

    @staticmethod
    # 获取哈希表中的字段
    def get_hash_field(hash_name, field):
        """
        获取哈希表中的字段
        """
        redis_client = get_redis_client()
        try:
            value = redis_client.hget(hash_name, field)
            if value is None:
                print(f"哈希 {hash_name} 中的字段 {field} 不存在")
            else:
                print(f"哈希 {hash_name} 中的字段 {field} 的值是: {value.decode('utf-8')}")
            return value
        except redis.exceptions.RedisError as e:
            print(f"获取哈希 {hash_name} 中字段 {field} 失败: {e}")
            return None

    @staticmethod
    # 设置列表值（从左侧推入）
    def push_to_list(list_name, value):
        """
        将值推入列表的左侧
        """
        redis_client = get_redis_client()
        try:
            redis_client.lpush(list_name, value)
            print(f"值 {value} 推入到列表 {list_name} 左侧成功")
        except redis.exceptions.RedisError as e:
            print(f"推入值 {value} 到列表 {list_name} 失败: {e}")

    @staticmethod
    # 从列表中弹出值（从左侧弹出）
    def pop_from_list(list_name):
        """
        从列表的左侧弹出一个值
        """
        redis_client = get_redis_client()
        try:
            value = redis_client.lpop(list_name)
            if value is None:
                print(f"列表 {list_name} 为空")
            else:
                print(f"从列表 {list_name} 弹出的值是: {value.decode('utf-8')}")
            return value
        except redis.exceptions.RedisError as e:
            print(f"从列表 {list_name} 弹出值失败: {e}")
            return None

    # 检查键是否存在
    @staticmethod
    def exists(key):
        """
        检查指定的键是否存在
        """
        redis_client = get_redis_client()
        try:
            return redis_client.exists(key)
        except redis.exceptions.RedisError as e:
            print(f"检查键 {key} 是否存在失败: {e}")
            return False

    @staticmethod
    # 设置过期时间
    def set_expiration(key, seconds):
        """
        设置键的过期时间（单位：秒）
        """
        redis_client = get_redis_client()
        try:
            redis_client.expire(key, seconds)
            print(f"键 {key} 的过期时间设置为 {seconds} 秒")
        except redis.exceptions.RedisError as e:
            print(f"设置键 {key} 过期时间失败: {e}")
