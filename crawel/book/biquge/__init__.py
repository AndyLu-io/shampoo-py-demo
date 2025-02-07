import requests
from bs4 import BeautifulSoup

# 目标URL
url = 'https://www.biquge11.cc/top/'

# 设置请求头，模拟浏览器请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def fetch_top_books(url):
    try:
        # 发送GET请求获取网页内容
        response = requests.get(url, headers=headers)

        # 判断请求是否成功
        if response.status_code != 200:
            print(f"请求失败，状态码: {response.status_code}")
            return []

        # 解析HTML页面
        soup = BeautifulSoup(response.content, 'html.parser')

        # 假设书籍的标题和链接都在 <div class="book-list"> 下，具体的类名需要根据页面分析调整
        book_list = []
        books = soup.find_all('div', class_='book-item')  # 根据实际页面结构选择合适的标签和类名

        # 遍历书籍，提取书名和链接
        for book in books:
            title_tag = book.find('a')  # 找到书名链接
            if title_tag:
                title = title_tag.get_text(strip=True)
                link = title_tag.get('href')
                book_list.append((title, link))

        return book_list

    except requests.RequestException as e:
        print(f"请求出错: {e}")
        return []


# 执行爬取
top_books = fetch_top_books(url)

# 打印获取到的书籍信息
if top_books:
    print("排名前几的书籍：")
    for i, (title, link) in enumerate(top_books, 1):
        print(f"{i}. {title} - {link}")
else:
    print("没有获取到书籍信息")
