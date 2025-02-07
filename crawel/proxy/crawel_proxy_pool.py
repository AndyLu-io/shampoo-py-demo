from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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


def fetch_proxy_pool(url):
    try:
        driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
        driver.get(url)

        ip_detail_elements = driver.find_elements(By.CSS_SELECTOR, "#ct-main  main  table  tbody  tr")
        get_ip_detail(ip_detail_elements)


    except Exception as e:
        print(f"爬取失败: {e}")
    finally:
        driver.quit()


def get_ip_detail(ip_detail_elements):
    for ip_detail_element in ip_detail_elements:
        text_elements = ip_detail_element.find_elements(By.CSS_SELECTOR, " td.text-monospace")
        ip = text_elements[0].text.strip()
        port = text_elements[1].text.strip()
        print(f"ip: {ip}, port: {port}")


fetch_proxy_pool("https://cn.proxy-tools.com/proxy/cn?page=1")
