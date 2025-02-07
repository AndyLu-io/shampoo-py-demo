from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

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


def fetch_book_chapter(book):
    try:
        driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
        driver.get(book.book_url)
        # time.sleep(3)  # 等待页面加载
        chapter_elements = driver.find_elements(By.CSS_SELECTOR, "#list dl dd")
        chapter_list = get_chapter_list(chapter_elements, book)
        save_chapter_list(chapter_list)
        new_book = {
            "book_name": book.book_name,
            'book_source': "beqege",
            'finish_flag': 1,
        }
        BookInfoDAO.update_book_info_by_source_and_name(book.book_source, book.book_name, new_book)

    except Exception as e:
        print(f"爬取失败: {e}")

    finally:
        driver.quit()


def save_chapter_list(chapter_list):
    for chapter in chapter_list:
        record = BookChapterDAO.get_chapter_by_source_name_and_chapter(chapter['book_source'], chapter['book_name'],
                                                                       chapter['chapter_name'])
        if record is None:
            BookChapterDAO.add_book_chapter(chapter)
        else:
            print(f"章节已存在: {chapter['chapter_name']}")


def get_chapter_list(chapter_elements, book):
    chapter_list = []
    chapter_index = 1
    for chapter_element in chapter_elements:
        chapter_name = chapter_element.find_element(By.CSS_SELECTOR, "a").text.strip()
        chapter_url = chapter_element.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        chapter_list.append({
            "book_name": book.book_name,
            "book_author": book.book_author,
            "book_desc": book.book_desc,
            'book_source': "beqege",
            'book_site': "https://www.beqege.cc/",
            "chapter_name": chapter_name,
            "chapter_url": chapter_url,
            "chapter_index": chapter_index
        })
        chapter_index += 1
        print(f"章节名: {chapter_name}, 章节链接: {chapter_url}")
    return chapter_list


if __name__ == '__main__':
    books = BookInfoDAO.list_all_book_infos()
    executor = ThreadPoolExecutor(max_workers=8)
    for book in books:
        if book.finish_flag != 1:
            executor.submit(fetch_book_chapter, book)
    executor.shutdown(wait=True)
