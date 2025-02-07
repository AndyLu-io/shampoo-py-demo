from concurrent.futures import ThreadPoolExecutor
from time import sleep

from crawel.book.mq.book.produce.rabbit_send_util import send_message, initialize_rabbitmq
from crawel.book.mq.rabbit_constans import RabbitKey


def send_book_info_task(url):
    send_message(RabbitKey.BOOK_INFO_QUEUE, url)

if __name__ == '__main__':
    initialize_rabbitmq()
    # executor = ThreadPoolExecutor(max_workers=4)
    for i in range(1, 104821):
        url = f"https://www.beqege.cc/top/{i}"
        try:
            # executor.submit(send_book_info_task, url)
            send_book_info_task(url)
            # sleep(0.01)
        except Exception as e:
            # initialize_rabbitmq()
            send_book_info_task(url)
    # executor.shutdown(wait=True)
