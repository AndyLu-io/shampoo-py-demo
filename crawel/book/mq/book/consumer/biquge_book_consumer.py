from crawel.book.mq.book.consumer.rabbit_consume_util import start_consuming, start_multiple_consumers
from crawel.book.mq.rabbit_constans import RabbitKey

if __name__ == '__main__':
    # start_consuming(RabbitKey.BIQUGE_BOOK_QUEUE)  # 启动消费指定队列

    queue_name = RabbitKey.BIQUGE_BOOK_QUEUE  # 选择你的队列
    num_consumers = 4  # 设置消费者数量（线程池大小）
    start_multiple_consumers(queue_name, num_consumers)  #