import requests

url = "https://wx.maoyan.com/maoyansh/myshow/ajax/tx/order/create"
headers = {
    "Host": "wx.maoyan.com",
    "Connection": "keep-alive",
    "Content-Length": "5584",
    "a7": "wxdbb4c5f1b8ee7da1",
    "x0": "3",
    "d1": "f5e1e733d09b41341131a0c3e4c3096f",
    "content-type": "application/json",
    "x-wxa-query": '{"performance_id":"366138"}',
    "x-wxa-referer": "pages/showsubs/ticket-level/v2/index",
    "uuid": "61232c078af99235d38b24c687b93336",
    "version": "wallet-v5.11.24",
    "X-Requested-With": "wxapp",
    "x-wxa-page": "pages/showsubs/order/confirm",
    "X-Channel-ID": "70001",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wxdbb4c5f1b8ee7da1/1569/page-frame.html"
}

# JSON data (body of the request)
json_data = {
    "token": "MY_700t8KrQYFhKaD55-fp7yPb64soAAAAwv66FKiPpe2w_bF1BreKnhbPQBcbYE53te7KqYZ15mDH-_aXWL7lg1_p--6g3gzoJAAAAqwAAAAEB",
    "sellChannel": 7,
    "uuid": "61232c078af99235d38b24c687b93336",
    "clientVersion": "8.0.47",
    "dpId": "61232c078af99235d38b24c687b93336",
    "lng": 120.39365912543403,
    "lat": 30.329481065538193,
    "clientPlatform": 2,
    "cityId": 50
}

# 发送 POST 请求
response = requests.post(url, headers=headers, json=json_data)

# 输出返回内容
print(response.text)
