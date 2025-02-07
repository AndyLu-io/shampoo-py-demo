import requests
from bs4 import BeautifulSoup

# 设置用户代理，避免被识别为爬虫
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 目标URL，可以替换为京东上的某个商品页面URL
url = 'https://item.jd.com/100012043978.html'

# 发送GET请求
response = requests.get(url, headers=headers)

# 确保请求成功
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # 示例：获取商品标题
    title = soup.select('body > div:nth-child(11) > div > div.itemInfo-wrap > div.sku-name')[0].text.strip()
    print("商品标题:", title)

    # 示例：获取商品价格（根据页面的结构可能需要调整）
    price = soup.find('span', class_='price').get_text().strip()
    print("商品价格:", price)

    # 进一步抓取其他信息
    # ... 根据页面结构抓取更多信息
else:
    print("请求失败，状态码：", response.status_code)
