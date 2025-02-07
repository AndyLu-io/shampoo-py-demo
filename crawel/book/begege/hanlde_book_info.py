import threading

from crawel.book.begege.book_info_crawel import fetch_book_list_hot
from crawel.book.db.dao.book_category_dao import BookCategoryDAO


def get_all_category(book_source):
    book_category = BookCategoryDAO.get_category_by_book_source(book_source)
    return book_category

# book_category_list = get_all_category("beqege")
# for category in book_category_list:
#     category_name_list=["首页", "完本小说", "排行榜单", "永久书架"]
#     if category.category_name not in category_name_list:
#         fetch_book_list_hot(category.category_url)

# 多线程执行任务
def fetch_books_for_category(category):
    category_name_list = ["首页", "完本小说", "排行榜单", "永久书架"]
    if category['category_name'] not in category_name_list:
        fetch_book_list_hot(category['category_url'])

def main():
    # 获取所有的类别
    book_category_list = get_all_category("beqege")

    # 创建一个线程列表
    threads = []

    # 遍历所有类别并为每个类别创建一个线程
    for category in book_category_list:
        # 为每个类别启动一个新线程
        thread = threading.Thread(target=fetch_books_for_category, args=(category,))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print("所有任务已完成")


if __name__ == "__main__":
    main()