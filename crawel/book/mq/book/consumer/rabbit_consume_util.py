import pika
import time

from crawel.book.mq.book.consumer.handle.base_message_handler import BaseMessageHandler
from crawel.book.mq.book.consumer.handle.biquge_book_handle import BiQuGeBookMessageHandler
from crawel.book.mq.book.consumer.handle.book_info_handle import BookInfoMessageHandler
from crawel.book.mq.rabbit_constans import RabbitKey

# 全局连接和通道
connection = None
channel = None

MAX_RETRIES = 5
RETRY_INTERVAL = 5  # 秒

# 消息处理器变量
message_handler: BaseMessageHandler = None  # 这里可以根据队列名动态加载不同的处理类


# 初始化连接和通道
def initialize_rabbitmq():
    global connection, channel
    retries = 0
    while retries < MAX_RETRIES:
        try:
            if connection is None or not connection.is_open:
                # 创建连接
                connection = pika.BlockingConnection(pika.ConnectionParameters(RabbitKey.DOMAIN))
                print("连接到 RabbitMQ 成功")

            if channel is None or channel.is_closed:
                # 创建通道
                channel = connection.channel()
                print("通道创建成功")

            # 声明 Exchange 和队列，避免重复声明
            channel.exchange_declare(exchange=RabbitKey.EXCHANGE, exchange_type='direct', durable=True)
            return channel  # 返回通道
        except pika.exceptions.AMQPConnectionError as e:
            print(f"连接失败，正在重试... {e}")
            retries += 1
            time.sleep(RETRY_INTERVAL)  # 等待一段时间后重试
        except Exception as e:
            print(f"发生其他错误: {e}")
            retries += 1
            time.sleep(RETRY_INTERVAL)

    raise Exception("重试超过最大次数，无法连接到 RabbitMQ")


# 根据队列名选择对应的消息处理类
def get_message_handler(queue_name: str) -> BaseMessageHandler:
    if queue_name == RabbitKey.BOOK_INFO_QUEUE:
        return BookInfoMessageHandler()  # 为书籍信息队列选择具体的处理类
    elif queue_name == RabbitKey.BIQUGE_BOOK_QUEUE:
        return BiQuGeBookMessageHandler()  # 为书籍信息队列选择具体的处理类
    else:
        # 其他队列的处理类可以在这里扩展
        raise ValueError(f"未找到处理器：{queue_name}")


# 处理接收到的消息
def callback(ch, method, properties, body):
    print(f"接收到消息: {body.decode()}")
    try:
        # 使用动态加载的处理类处理消息
        if message_handler:
            message_handler.process_message(body.decode())

        # 手动确认消息已经处理成功
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print("消息已确认")
    except Exception as e:
        # 出现异常时，拒绝消息并不确认
        print(f"处理消息失败: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
        print("消息未确认，已重新入队")


# 启动消费者，支持不同的队列和处理策略
def start_consuming(queue_name: str):
    global channel, message_handler
    try:
        if channel is None or not channel.is_open:
            channel = initialize_rabbitmq()

        # 根据队列名选择消息处理器
        message_handler = get_message_handler(queue_name)

        # 声明队列并绑定到交换机
        channel.queue_declare(queue=queue_name, durable=True)  # 确保队列持久化
        channel.queue_bind(exchange=RabbitKey.EXCHANGE,
                           queue=queue_name,
                           routing_key=queue_name)

        # 设置消费者，指定队列以及消费回调函数
        channel.basic_consume(queue=queue_name,
                              on_message_callback=callback,  # 消费回调
                              auto_ack=False)  # 禁止自动确认
        print(f'等待接收消息，队列：{queue_name}，按 CTRL+C 停止')
        channel.start_consuming()  # 启动消费循环
    except Exception as e:
        print(f"消费者启动失败: {e}")
        # 出现异常时，关闭连接和通道
        close_rabbitmq()


# 关闭 RabbitMQ 连接和通道
def close_rabbitmq():
    global connection, channel
    if connection and channel:
        channel.close()
        connection.close()
        connection = None
        channel = None
        print("连接和通道已关闭")


