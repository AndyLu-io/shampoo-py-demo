from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 设置 Chrome 无头模式
options = Options()
options.add_argument('--headless')  # 无头模式
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# 设置 chromedriver 路径
CHROMEDRIVER_PATH = "/Users/luxiaobo/Documents/chromedriver-mac-arm64/chromedriver"

# 启动 Chrome 浏览器
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

def fetch_chapter_content(url):
    """使用 Selenium 获取章节内容"""
    try:
        driver.get(url)
        time.sleep(3)  # 等待页面加载

        # 获取章节标题
        title = driver.find_element(By.TAG_NAME, 'h1').text.strip()

        # 获取章节正文内容
        content_div = driver.find_element(By.ID, 'content')
        paragraphs = content_div.text.strip()

        return {"title": title, "content": paragraphs}
    except Exception as e:
        print(f"爬取失败：{e}")
        return None

# 测试爬取某章节
url = "https://www.beqege.cc/1076/14341496.html"
chapter = fetch_chapter_content(url)

if chapter:
    print(f"章节标题: {chapter['title']}")
    print(f"章节内容:\n{chapter['content']}")

    # 保存到文件
    with open(f"{chapter['title']}.txt", "w", encoding="utf-8") as f:
        f.write(chapter['title'] + "\n\n")
        f.write(chapter['content'])
        print(f"章节已保存为 {chapter['title']}.txt")

# 关闭浏览器
driver.quit()
