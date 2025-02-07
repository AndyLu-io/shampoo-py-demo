from crawel.book.redis.redis_util import RedisUtil

if __name__ == '__main__':
    RedisUtil.set_value("aa", "shamppootest")
    value = RedisUtil.get_value("aa")
    print(value)
