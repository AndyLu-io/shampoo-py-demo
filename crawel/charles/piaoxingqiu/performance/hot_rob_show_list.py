import requests

from crawel.charles.piaoxingqiu.constants.piao_contants import PiaoConstans

# 请求的 URL
url = "https://m.piaoxingqiu.com/cyy_gatewayapi/home/pub/v3/floors/hot_rob"
params = {
    "cityId": "BL1120",
    "lang": "zh",
    "src": "weixin_mini",
    "merchantId": "6267a80eed218542786f1494",
    "ver": "4.23.4",
    "appId": "wxad60dd8123a62329"
}

# 请求头
headers = {
    "Host": PiaoConstans.HOST,
    "Connection": "keep-alive",
    "terminal-src": "WEIXIN_MINI",
    "content-type": "application/json",
    "src": "weixin_mini",
    "ver": "4.23.4",
    "access-token": PiaoConstans.AUTH_TOKEN,
    "merchant-id": PiaoConstans.MERCHANT_ID,
    "front-trace-id": "m4y0536anvxzf6tffj",
    "Angry-dog": PiaoConstans.ANGRY_DOG,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wxad60dd8123a62329/312/page-frame.html"
}

# 发起 GET 请求
response = requests.get(url, headers=headers, params=params)
hot_shows = response.json().get('data').get('current')
for show in hot_shows:
    print(show)
# # 输出请求结果
# print("返回状态码:", response.status_code)
# print("返回内容:", response.text)
