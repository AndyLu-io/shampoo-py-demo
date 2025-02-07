from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from crawel.book.db.dao.book_category_dao import BookCategoryDAO
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


# 创建 Selenium 服务
# service = Service(CHROMEDRIVER_PATH)
# driver = webdriver.Chrome(service=service, options=options)


def get_hot_books(hot_content_elements):
    hot_books = []
    for hot_content_element in hot_content_elements:
        book_name = hot_content_element.find_element(By.CSS_SELECTOR, "dl dt a").text.strip()
        book_url = hot_content_element.find_element(By.CSS_SELECTOR, "dl dt a").get_attribute("href")
        book_img = hot_content_element.find_element(By.CSS_SELECTOR, "div.image a img").get_attribute("src")
        book_author = hot_content_element.find_element(By.CSS_SELECTOR, "dl dt span").text.strip()
        book_desc = hot_content_element.find_element(By.CSS_SELECTOR, "dl dd").text.strip()
        hot_books.append({
            "book_name": book_name,
            "book_url": book_url,
            "book_img": book_img,
            "book_author": book_author,
            "book_desc": book_desc,
            'book_source': "beqege",
            'book_site': "https://www.beqege.cc/",

        })
    return hot_books


def update_book(new_content_elements):
    update_books = []
    for new_content_hot_element in new_content_elements:
        book_name = new_content_hot_element.find_element(By.CSS_SELECTOR, "span.s2 a").text.strip()
        book_url = new_content_hot_element.find_element(By.CSS_SELECTOR, "span.s2 a").get_attribute("href")
        book_author = new_content_hot_element.find_element(By.CSS_SELECTOR, "span.s4").text.strip()
        # book_desc = new_content_hot_element.find_element(By.CSS_SELECTOR, "s5").text.strip()
        update_books.append({
            "book_name": book_name,
            "book_url": book_url,
            "book_author": book_author,
            # "book_desc": book_desc,
            'book_source': "beqege",
            'book_site': "https://www.beqege.cc/",
        })
    return update_books


def hot_book(new_content_hot_elements):
    new_hot_books = []
    for new_content_hot_element in new_content_hot_elements:
        book_name = new_content_hot_element.find_element(By.CSS_SELECTOR, "span.s2 a").text.strip()
        book_url = new_content_hot_element.find_element(By.CSS_SELECTOR, "span.s2 a").get_attribute("href")
        book_author = new_content_hot_element.find_element(By.CSS_SELECTOR, "span.s5").text.strip()
        # book_desc = new_content_hot_element.find_element(By.CSS_SELECTOR, "s5").text.strip()
        new_hot_books.append({
            "book_name": book_name,
            "book_url": book_url,
            "book_author": book_author,
            # "book_desc": book_desc,
            'book_source': "beqege",
            'book_site': "https://www.beqege.cc/",

        })
    return new_hot_books


def fetch_book_list_hot(url):
    try:
        driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
        driver.get(url)

        result_books = []
        hot_content_elements = driver.find_elements(By.CSS_SELECTOR, "#hotcontent div.ll div.item")
        new_content_elements = driver.find_elements(By.CSS_SELECTOR, "#newscontent div.l ul li")
        new_content_hot_elements = driver.find_elements(By.CSS_SELECTOR, "#newscontent div.r ul li")
        hot_books = get_hot_books(hot_content_elements)
        update_books = update_book(new_content_elements)
        hot_book_list = hot_book(new_content_hot_elements)
        result_books.extend(hot_books)
        result_books.extend(update_books)
        result_books.extend(hot_book_list)
        for book in result_books:
            print(f"书名: {book['book_name']}, 链接: {book['book_url']}, 作者: {book['book_author']}")
        store_books(result_books)

    except Exception as e:
        print(f"爬取失败: {e}")
    finally:
        driver.quit()


def store_books(hot_books):
    for book in hot_books:
        # 检查数据库中是否已经存在该书籍，避免重复插入
        existing_book = BookInfoDAO.get_book_info_by_source_and_name(book['book_source'], book['book_name'])
        if existing_book is None:
            BookInfoDAO.add_book_info(book)


book_category_list = BookCategoryDAO.get_category_by_book_source("beqege")
for category in book_category_list:
    category_name_list = ["首页", "完本小说", "排行榜单", "永久书架"]
    if category.category_name not in category_name_list:
        fetch_book_list_hot(category.category_url)

# fetch_book_list_hot("https://www.beqege.cc/class2/")

