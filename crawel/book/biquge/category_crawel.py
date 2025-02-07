import requests
from bs4 import BeautifulSoup

# 设置请求头，模拟浏览器请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def fetch_date_list(url):
    try:
        # 发送GET请求获取网页内容
        response = requests.get(url, headers=headers)

        # 判断请求是否成功
        if response.status_code != 200:
            print(f"请求失败，状态码: {response.status_code}")
            return None

        # 解析HTML页面
        soup = BeautifulSoup(response.content, 'html.parser')

        select_element = soup.select('body > div.main > div.main-content > div.framecontent > div.title-wrap-auto > div.right > div > select')
        date_elements = soup.select
        date_list = []
        for element in date_elements:
            date_list.append(element.text.strip() if element else None)

        print(date_list)

    except requests.RequestException as e:
        print(f"请求出错: {e}")
        return None

fetch_date_list('https://data.eastmoney.com/zlsj/2023-12-31-1-2.html')
