import requests
import json

from crawel.charles.maoyan.constants.maoyan_constants import MaoYanConstants

# 请求的 URL
url = 'https://wx.maoyan.com/my/odea/project/shows'

def fetch_show_list(projectId):

    # 请求头部信息
    headers = {
         'Host': MaoYanConstants.HOST,
        'Connection': 'keep-alive',
        'Content-Length': '22',
        'a7': 'wxdbb4c5f1b8ee7da1',
        'x0': '3',
        'd1': 'c1be67578a9af01207ccc9c821358509',
        'Content-Type': 'application/json',
        'x-wxa-query': '%7B%22isNewPage%22%3A%22true%22%2C%22id%22%3A%22366138%22%2C%22isHotProject%22%3A%220%22%2C%22modelStyle%22%3A%220%22%7D',
        'x-wxa-referer': 'pages/show/detail/v2/index',
        'uuid': '61232c078af99235d38b24c687b93336',
        'version': 'wallet-v5.11.24',
        'X-Requested-With': 'wxapp',
        'x-wxa-page': 'pages/showsubs/ticket-level/v2/index',
        'token': MaoYanConstants.AUTH_TOKEN,
        'X-Channel-ID': '70001',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN',
        'Referer': 'https://servicewechat.com/wxdbb4c5f1b8ee7da1/1569/page-frame.html'
    }

    # 请求体数据
    data = {
        "projectId": projectId
    }

    # 发送 POST 请求
    response = requests.post(url, headers=headers, json=data)

    # 打印响应内容
    if response.status_code == 200:
        show_list = response.json().get('data').get('showListVO')
        for show in show_list:
            print(show)
        # 如果是 JSON 响应，直接解析为 JSON 格式
    else:
        print(f"请求失败，状态码: {response.status_code}")


fetch_show_list(366138)
