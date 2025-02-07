import requests
from bs4 import BeautifulSoup


def fetch_douban_chart():
    url = "https://movie.douban.com/chart"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    # 确认请求成功
    if response.status_code != 200:
        print(f"请求失败，状态码：{response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # 找到所有电影的条目
    movies = soup.find_all("tr", class_="item")

    # 存储电影数据
    movie_data = []

    for movie in movies:
        title_tag = movie.find("a", title=True)
        title = title_tag["title"] if title_tag else "未知"

        link = title_tag["href"] if title_tag else "未知"

        # 获取额外信息
        info_tag = movie.find("p", class_="pl")
        info = info_tag.text.strip() if info_tag else "无相关信息"

        movie_data.append({
            "title": title,
            "link": link,
            "info": info
        })

    return movie_data


if __name__ == "__main__":
    movies = fetch_douban_chart()
    if movies:
        for idx, movie in enumerate(movies, start=1):
            print(f"{idx}. {movie['title']}")
            print(f"   链接: {movie['link']}")
            print(f"   信息: {movie['info']}")
            print()
