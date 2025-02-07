import pika
import time
from crawel.book.mq.rabbit_constans import RabbitKey

MAX_RETRIES = 5
RETRY_INTERVAL = 5  # 秒

connection = None
channel = None
def initialize_rabbitmq():
    global connection, channel
    retries = 0
    while retries < MAX_RETRIES:
        try:
            if connection is None or not connection.is_open:
                # 创建连接
                connection = pika.BlockingConnection(pika.ConnectionParameters(RabbitKey.DOMAIN))
                print("连接到 RabbitMQ 成功")

            # 创建通道
            channel = connection.channel()
            # 声明 Exchange
            channel.exchange_declare(exchange=RabbitKey.EXCHANGE, exchange_type='direct', durable=True)
            # 声明队列
            channel.queue_declare(queue=RabbitKey.BOOK_INFO_QUEUE, durable=True)
            # 绑定队列到 Exchange
            channel.queue_bind(exchange=RabbitKey.EXCHANGE,
                               queue=RabbitKey.BOOK_INFO_QUEUE,
                               routing_key=RabbitKey.BOOK_INFO_QUEUE)

            # ================================================================================================
            # 声明队列
            channel.queue_declare(queue=RabbitKey.BIQUGE_BOOK_QUEUE, durable=True)
            # 绑定队列到 Exchange
            channel.queue_bind(exchange=RabbitKey.EXCHANGE,
                               queue=RabbitKey.BIQUGE_BOOK_QUEUE,
                               routing_key=RabbitKey.BIQUGE_BOOK_QUEUE)

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


def send_message(routing_key, message):
    channel = connection.channel() # 每次调用初始化通道
    try:
        channel.basic_publish(exchange=RabbitKey.EXCHANGE,
                              routing_key=routing_key,
                              body=message)
        print(f" [x] Sent message with routing_key '{routing_key}': {message}")
        # 完成后关闭通道，释放资源
    except Exception as e:
        print(f"发送失败: {e}")

    finally:
        channel.close()

    # 发送消息



def close_rabbitmq():
    global connection, channel
    if connection and channel:
        connection.close()
        connection = None
        channel = None
        print(" [x] Connection closed")
