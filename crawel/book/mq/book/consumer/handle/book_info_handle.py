from crawel.book.begege.book_detail_crawel import fetch_book_detail, update_book_detail
from crawel.book.mq.book.consumer.handle.base_message_handler import BaseMessageHandler


class BookInfoMessageHandler(BaseMessageHandler):

    def process_message(self, message: str):
        # 这里是你的特定消息处理逻辑
        new_book = fetch_book_detail(message)
        update_book_detail(new_book)

