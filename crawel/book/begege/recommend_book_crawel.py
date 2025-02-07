from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from crawel.book.begege.book_detail_crawel import update_book_detail
from crawel.book.db.dao.book_chapter_dao import BookChapterDAO
from crawel.book.db.dao.book_info_dao import BookInfoDAO

# 替换为实际的 chromedriver 路径
CHROMEDRIVER_PATH = "/Users/luxiaobo/Documents/chromedriver-mac-arm64/chromedriver"

# 配置 Selenium 无头模式
options = Options()
options.add_argument("--headless")  # 无头模式
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")


def fetch_recommend_book(url):
    try:
        driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
        driver.get(url)

        recommend_book_elements = driver.find_elements(By.CSS_SELECTOR, '#listtj a')
        for element in recommend_book_elements:
            book_name = element.text.strip()
            book_url = element.get_attribute("href")
            book = {
                "book_name": book_name,
                "book_url": book_url,
                'book_source': "beqege",
                'book_site': "https://www.beqege.cc/",
            }
            print(f"书名: {book['book_name']}, 链接: {book['book_url']}")

            update_book_detail(book)

    except Exception as e:
        print(f"爬取失败: {e}")

    finally:
        driver.quit()


if __name__ == '__main__':
    books = BookInfoDAO.list_all_book_infos()
    executor = ThreadPoolExecutor(max_workers=4)
    for book in books:
        executor.submit(fetch_recommend_book, book.book_url)
    executor.shutdown(wait=True)
