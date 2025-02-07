from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from crawel.book.db.dao.book_top_dao import BookTopDAO

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

# 创建 Selenium 服务
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)


def fetch_book_top(url):
    try:
        driver.get(url)
        time.sleep(3)  # 等待页面加载

        # 定位到包含书籍信息的 ul 标签
        rank_elements = driver.find_elements(By.CSS_SELECTOR, "div.layout-col1")

        for element in rank_elements:
            rank_name_element = element.find_elements(By.CSS_SELECTOR, "div.layout-tit strong")
            rank_name = rank_name_element[0].text.strip()
            book_elements = element.find_elements(By.CSS_SELECTOR, "div.tab-bd ul.txt-list-row3 li")
            books = get_books(book_elements, rank_name)
            # 输出爬取的书籍信息
            for book in books:
                print(f"书名: {book['book_name']}, 链接: {book['book_url']}")

            store_book_top(books, rank_name)


    except Exception as e:
        print(f"爬取失败: {e}")
    finally:
        driver.quit()


def get_books(book_elements, rank_name):
    books = []
    for book_element in book_elements:
        # 提取书籍名称
        book_name = book_element.find_element(By.CSS_SELECTOR, "span.s2 a").text.strip()
        # 提取书籍链接
        book_url = book_element.find_element(By.CSS_SELECTOR, "span.s2 a").get_attribute("href")

        # 排除空链接或无效链接
        if book_name and book_url:
            book = {
                'book_name': book_name,
                'book_url': book_url,
                'book_source': "beqege",
                'book_site': "https://www.beqege.cc/",
                'rank_name': rank_name

            }
            books.append(book)

    return books


def store_book_top(books, rank_list_name):
    for book in books:
        # 检查数据库中是否已经存在该书籍，避免重复插入
        existing_book = BookTopDAO.get_book_top_by_rank_and_book_name(book['book_source'], rank_list_name,
                                                                      book['book_name'])
        if existing_book is None:
            # 将书籍信息添加到数据库
            book_data = {
                'rank_list_name': rank_list_name,
                'book_name': book['book_name'],
                'book_url': book['book_url'],
                'book_source': book['book_source'],
                'book_site': book['book_site']
            }
            BookTopDAO.add_book_top(book_data)
        else:
            print(f"书籍 '{book['book_name']}' 已存在，跳过存储。")


# 访问网站并获取书籍信息
url = "https://www.beqege.cc/top/"  # 替换为你想爬取的 URL
books = fetch_book_top(url)



