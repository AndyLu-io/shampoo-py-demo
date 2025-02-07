import pika

# 连接到 RabbitMQ 服务器
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 声明一个队列
channel.queue_declare(queue='hello')

# 定义回调函数，处理接收到的消息
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# 告诉 RabbitMQ 使用 callback 函数来处理 'hello' 队列中的消息
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press Ctrl+C')
# 启动消费过程
channel.start_consuming()
