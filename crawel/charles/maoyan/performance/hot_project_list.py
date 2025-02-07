import requests

from crawel.charles.maoyan.constants.maoyan_constants import MaoYanConstants

# 目标 URL
url = 'https://wx.maoyan.com/maoyansh/myshow/ajax/channelPage/wonderPerfs'

def fetch_hot_project_list():
    # 请求参数
    params = {
        'p': 1,
        's': 20,
        'ct': 1,
        'st': 4,
        'token': MaoYanConstants.AUTH_TOKEN,
        'sellChannel': 7,
        'clientPlatform': 2,
        'cityId': 50,
        'x-wxa-query': '{"categoryId":1,"city_id":50,"category":"演唱会","category_id":1,"searchTypeFromWx":0}'
    }

    # 请求头
    headers = {
        'Host': MaoYanConstants.HOST,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'x-wxa-referer': 'pages/movie/index',
        'uuid': '61232c078af99235d38b24c687b93336',
        'version': 'wallet-v5.11.24',
        'X-Requested-With': 'wxapp',
        'x-wxa-page': 'pages/show/list/index',
        'X-Channel-ID': '70001',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN',
        'Referer': 'https://servicewechat.com/wxdbb4c5f1b8ee7da1/1569/page-frame.html'
    }

    # 发送 GET 请求
    response = requests.get(url, params=params, headers=headers)

    # 检查响应状态
    if response.status_code == 200:
        # 解析 JSON 数据
        data = response.json()
        hot_show_list =  data.get("data")
        for show in hot_show_list:
            print(show)
    else:
        print(f"请求失败，状态码: {response.status_code}")


fetch_hot_project_list()