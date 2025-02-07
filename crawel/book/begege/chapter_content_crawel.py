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


def fetch_chapter_content(url):
    """使用 Selenium 获取章节内容"""
    try:
        driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
        driver.get(url)
        time.sleep(3)  # 等待页面加载

        # 获取章节标题
        title = driver.find_element(By.TAG_NAME, 'h1').text.strip()

        # 获取章节正文内容
        content_div = driver.find_element(By.ID, 'content')
        paragraphs = content_div.text.strip()

        print("title" + title + "content" + paragraphs)
    except Exception as e:
        print(f"爬取失败：{e}")
        return None
    finally:
        driver.quit()


if __name__ == '__main__':
    fetch_chapter_content("https://www.beqege.cc/1219/16251714.html")
# da从数据库中获取书籍信息

