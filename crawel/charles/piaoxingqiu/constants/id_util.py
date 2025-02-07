import random
import time


def generate_order_number():
    # 获取当前 Unix 时间戳的前 10 位
    timestamp = str(int(time.time()))[:10]

    # 随机生成4位数和3位数
    random_part1 = random.randint(1000, 9999)  # 4 位随机数
    random_part2 = random.randint(0, 999)  # 3 位随机数

    # 格式化成需要的格式
    order_number = f"{timestamp}{random_part1:04d}00000{random_part2:03d}"

    return order_number


# 示例生成单号
order_number = generate_order_number()
print(order_number)
