
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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


def fetch_book_detail(url):
    try:
        driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
        driver.get(url)
        # time.sleep(3)  # 等待页面加载

        book_name = driver.find_element(By.XPATH, '//*[@id="info"]/h1').text.strip()
        book_author = driver.find_element(By.XPATH, '//*[@id="info"]/p[1]').text.strip()
        book_desc = driver.find_element(By.XPATH, '//*[@id="intro"]/p[1]').text.strip()
        clean_book_author = book_author.replace("&nbsp;", "").replace("作", "").replace("者：", "").strip()
        # 定位 img 标签（按需要修改 selector）
        img_element = driver.find_element(By.XPATH, '//*[@id="fmimg"]/img')

        # 提取图片链接，优先获取 data-original，若无则获取 src
        book_img = img_element.get_attribute("data-original") or img_element.get_attribute("src")
        book_img = urljoin(url, book_img)

        book = {
            "book_name": book_name,
            "book_author": clean_book_author,
            "book_desc": book_desc,
            "book_img": book_img,
            'book_source': "beqege",
            'book_site': "https://www.beqege.cc/",
        }

        print(
            f"书名: {book['book_name']}, 作者: {book['book_author']}, 描述: {book['book_desc']}, 图片: {book['book_img']}")

        # store_books([book])
        return book

    except Exception as e:
        print(f"爬取失败: {e}")
    finally:
        driver.quit()


def update_book_detail(book):
    book_info = BookInfoDAO.get_book_info_by_source_and_name(book['book_source'], book['book_name'])
    if book_info:
        # 更新书籍信息
        BookInfoDAO.update_book_info_by_source_and_name(book['book_source'], book['book_name'], book)
    else:
        # 新增书籍信息
        BookInfoDAO.add_book_info(book)


def fetch_book_detail_handle(book):
    try:
        new_book = fetch_book_detail(book.book_url)
        update_book_detail(new_book)
    except BaseException as e:
        print(f'fetch_book_detail_handle 处理异常 {e}')


if __name__ == '__main__':
    # booklist = BookInfoDAO.list_all_book_infos()
    # executor = ThreadPoolExecutor(max_workers=4)
    # for book in booklist:
    #     if book.book_img is None:
    #         executor.submit(fetch_book_detail_handle, book)
    # executor.shutdown(wait=True)

    new_book = fetch_book_detail("https://www.beqege.cc/57103/")
    update_book_detail(new_book)