import requests
from bs4 import BeautifulSoup

from crawel.book.begege.book_detail_crawel import update_book_detail

# 设置请求头，模拟浏览器请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def fetch_book_detail(url):
    try:
        # 发送GET请求获取网页内容
        response = requests.get(url, headers=headers)

        # 判断请求是否成功
        if response.status_code != 200:
            print(f"请求失败，状态码: {response.status_code}")
            return None

        # 解析HTML页面
        soup = BeautifulSoup(response.content, 'html.parser')

        # 使用 XPath 查询（这里用 lxml 来实现 XPath）
        # 例如：通过 XPath /html/body/div[5]/div[2]/h1 获取该标签
        element = soup.select('body > div.book > div.info > h1')
        book_name = element[0].text.strip() if element else None
        book_author = soup.select('body > div.book > div.info > div.small > span:nth-child(1)')[0].text.strip()
        book_desc = soup.select('body > div.book > div.info > div.intro > dl > dd')[0].text.strip()
        clean_book_author = book_author.replace("&nbsp;", "").replace("作", "").replace("者：", "").strip()
        book_img = soup.select('body > div.book > div.info > div.cover > img')[0].get('src')
        book = {
            "book_name": book_name,
            "book_author": clean_book_author,
            "book_desc": book_desc,
            "book_img": book_img,
            "book_url": url,
            'book_source': "biquge11",
            'book_site': "https://www.biquge11.cc",
            'finish_flag': 0
        }

        print(
            f"书名: {book['book_name']}, 作者: {book['book_author']}, 描述: {book['book_desc']}, 图片: {book['book_img']}")

        update_book_detail(book)
        return book
    except requests.RequestException as e:
        print(f"请求出错: {e}")
        return None


if __name__ == '__main__':
    url = 'https://www.biquge11.cc/read/191632/'
    fetch_book_detail(url)