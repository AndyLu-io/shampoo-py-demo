from concurrent.futures import ThreadPoolExecutor

from crawel.book.begege.book_detail_crawel import fetch_book_detail, update_book_detail
from crawel.book.db.dao.book_info_dao import BookInfoDAO


def fetch_book_detail_all(url):
    try:
        new_book = fetch_book_detail(url)
        update_book_detail(new_book)
    except BaseException as e:
        print(f'fetch_book_detail_handle 处理异常 {e}')


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=8)
    for i in range(5000, 104820):
        url = f"https://www.beqege.cc/top/{i}"
        executor.submit(fetch_book_detail_all, url)
        # book_info = BookInfoDAO.get_by_book_url(url)
        # if book_info is None:
    executor.shutdown(wait=True)
