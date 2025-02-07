import requests

from crawel.charles.piaoxingqiu.constants.piao_contants import PiaoConstans

# 设置请求URL和参数
url = "https://m.piaoxingqiu.com/cyy_gatewayapi/home/pub/v3/show_list/search_by_front"

def fetch_show_list():

    # 设置请求头
    headers = {
        "Host": PiaoConstans.HOST,
        "Connection": "keep-alive",
        "terminal-src": "WEIXIN_MINI",
        "content-type": "application/json",
        "src": "weixin_mini",
        "ver": "4.23.4",
        "access-token": PiaoConstans.AUTH_TOKEN,
        "merchant-id": PiaoConstans.MERCHANT_ID,
        "front-trace-id": "m4wyyozctx2q4jppij",
        "Angry-dog": PiaoConstans.ANGRY_DOG,
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxad60dd8123a62329/312/page-frame.html"
    }

    params = {
        "bizFrontendCategoryId": PiaoConstans.bizFrontendCategoryId,
        "cityId": "BL1120",
        "lang": "zh",
        "length": 10,
        "offset": 0,
        "pageType": "ALL_PAGE",
        "sortType": "ATTENTION",
        "src": "weixin_mini",
        "merchantId": PiaoConstans.MERCHANT_ID,
        "ver": "4.23.4",
        "appId": PiaoConstans.APP_ID
    }

    # 发送GET请求
    response = requests.get(url, headers=headers, params=params)

    return response.json().get('data').get('searchData')



show_list = fetch_show_list()
for show in show_list:
    print(show)