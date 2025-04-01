import requests

from crawel.charles.piaoxingqiu.constants.piao_contants import PiaoConstans


def fetch_show_detail(show_id):
    # 请求 URL
    url = f"https://m.piaoxingqiu.com/cyy_gatewayapi/show/pub/v5/show/{show_id}/static"

    # 请求参数
    params = {
        "lang": "zh",
        "src": "weixin_mini",
        "merchantId": PiaoConstans.MERCHANT_ID,
        "ver": "4.23.4",
        "appId": PiaoConstans.APP_ID,
        "cityId": "BL1120",
        "source": "FROM_QUICK_ORDER",
        "siteId": "6268b1ff363f4f0a8254300d",
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
        "front-trace-id": "m4xsw78zovnufuyipco",
        "Angry-dog": PiaoConstans.ANGRY_DOG,
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxad60dd8123a62329/312/page-frame.html"
    }

    # 发送 GET 请求
    response = requests.get(url, headers=headers, params=params)

    # 打印响应结果
    print(f"状态码: {response.status_code}")
    print(f"响应内容: {response.text}")


fetch_show_detail("67d6dc4499c2e800011bfa0f")