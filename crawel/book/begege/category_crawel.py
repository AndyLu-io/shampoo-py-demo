import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from crawel.book.db.dao.book_category_dao import BookCategoryDAO

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


def fetch_book_category(url):
    try:
        driver.get(url)
        time.sleep(3)  # 等待页面加载

        # 使用更新的选择器找到分类链接
        category_elements = driver.find_elements(By.CSS_SELECTOR, "div.nav ul li a")  # 根据实际HTML结构选择

        categories = []

        for element in category_elements:
            category_name = element.text.strip()
            category_url = element.get_attribute("href")

            # 只保存有效的分类信息
            if category_name and category_url:
                categories.append({"category_name": category_name, "category_url": category_url})

        return categories

    except Exception as e:
        print(f"爬取失败: {e}")
    finally:
        driver.quit()


def store_categories(categories):
    for category in categories:
        # 检查数据库中是否已经存在该分类，避免重复插入
        existing_category = BookCategoryDAO.get_category_by_name(category['category_name'])
        if existing_category is None:
            # 将分类信息添加到数据库
            category_data = {
                'book_source': "beqege",
                'book_site': "https://www.beqege.cc/",
                'category_name': category['category_name'],
                'category_url': category['category_url']
            }
            BookCategoryDAO.add_book_category(category_data)
        else:
            print(f"分类 '{category['category_name']}' 已存在，跳过存储。")



# 访问网站并获取类别信息
url = "https://www.beqege.cc/"
categories = fetch_book_category(url)

print(categories)

# 将爬取到的分类信息存储到数据库
store_categories(categories)


