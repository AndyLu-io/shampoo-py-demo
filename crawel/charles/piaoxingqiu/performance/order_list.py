import requests

from crawel.charles.piaoxingqiu.constants.piao_contants import PiaoConstans

# 请求 URL
url = "https://m.piaoxingqiu.com/cyy_gatewayapi/trade/buyer/order/v3/order_list?lang=zh&length=10&offset=0&orderStatusQuery=TERMINATED"

def fetch_order_list():

    # 请求头
    headers = {
        "Host": PiaoConstans.HOST,
        "Connection": "keep-alive",
        "Content-Length": "105",
        "terminal-src": "WEIXIN_MINI",
        "content-type": "application/json",
        "src": "weixin_mini",
        "ver": "4.23.4",
        "access-token": PiaoConstans.AUTH_TOKEN,
        "merchant-id": PiaoConstans.MERCHANT_ID,
        "front-trace-id": "m4xs1pzur35dhp8j80o",
        "Angry-dog": PiaoConstans.ANGRY_DOG,
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxad60dd8123a62329/312/page-frame.html"
    }

    # 请求体
    data = {
        "src": "weixin_mini",
        "merchantId": "6267a80eed218542786f1494",
        "ver": "4.23.4",
        "appId": "wxad60dd8123a62329"
    }

    # 发送 POST 请求
    response = requests.post(url, headers=headers, json=data)
    return response.json().get("data")




order_list = fetch_order_list()
for order in order_list:
    print(order)