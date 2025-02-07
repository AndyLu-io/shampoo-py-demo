import requests

# 请求的 URL
url = "https://mtop.damai.cn/h5/mtop.alibaba.damai.detail.getdetail/1.2/2.0/"

# 请求参数
params = {
    "jsv": "2.4.12",
    "appKey": "12574478",
    "t": "1734688592816",
    "sign": "cc22ef31e819b97c3a22ce55a8b60358",
    "c": "77998ecd5569404cf24072a9eb9fd167_1734686239530;1201d174bfff040e79f5fd7419915388",
    "v": "1.2",
    "dataType": "json",
    "type": "originaljson",
    "AntiCreep": "true",
    "AntiFlood": "true",
    "api": "mtop.alibaba.damai.detail.getdetail",
    "url": "mtop.alibaba.damai.detail.getdetail",
    "env": "m",
    "data": '{"dmChannel":"damai@weixin_weapp","itemId":"856424965356","lat":30.189733615451388,"lng":120.20178738064236}',
    "_bx-m": "0.0.11"
}

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wx5a8f481d967649eb/103/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

# 发起 GET 请求
response = requests.get(url, params=params, headers=headers)

# 检查响应
if response.status_code == 200:
    print("请求成功:", response.json())
else:
    print(f"请求失败，状态码: {response.status_code}, 响应内容: {response.text}")
