import requests

from crawel.charles.piaoxingqiu.constants.piao_contants import PiaoConstans


def fetch_session_list(show_id):
    # 请求的 URL 和查询参数
    url = f"https://m.piaoxingqiu.com/cyy_gatewayapi/show/pub/v5/show/{show_id}/sessions"
    params = {
        "lang": "zh",
        "src": "weixin_mini",
        "merchantId": PiaoConstans.MERCHANT_ID,
        "ver": "4.23.4",
        "appId": PiaoConstans.APP_ID,
        "source": "FROM_QUICK_ORDER",
        "isQueryShowBasicInfo": "true"
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
        "front-trace-id": "m4xtmswrqz6j59pne3g",
        "Angry-dog": PiaoConstans.ANGRY_DOG,
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxad60dd8123a62329/312/page-frame.html"
    }

    # 发起请求
    response = requests.get(url, params=params, headers=headers)

    return response.json().get("data")

    # 输出请求结果
    # print("完整请求 URL:", response.url)
    # print("返回状态码:", response.status_code)
    # print("返回内容:", response.text)


session_list = fetch_session_list('67d6dc4499c2e800011bfa0f')
for session in session_list:
    print(session['bizShowSessionId'])