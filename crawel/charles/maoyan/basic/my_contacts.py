import requests

# 请求的 URL 和查询参数
url = "https://wx.maoyan.com/maoyansh/myshow/ajax/tx/realName/allRealNameUserList"
def fetch_my_maoyan_contacts():
    params = {
        'projectId': '366138',
        'showId': '2284212',
        'token': 'MY_700t8KrQYFhKaD55-fp7yPb64soAAAAwv66FKiPpe2w_bF1BreKnhbPQBcbYE53te7KqYZ15mDH-_aXWL7lg1_p--6g3gzoJAAAAqwAAAAEB',
        'sellChannel': '7',
        'clientPlatform': '2',
        'cityId': '50'
    }

    # 请求头部
    headers = {
        'Content-Type': 'multipart/form-data',
        'x-wxa-query': '%7B%22performance_id%22%3A%22366138%22%7D',
        'x-wxa-referer': 'pages/showsubs/ticket-level/v2/index',
        'uuid': '61232c078af99235d38b24c687b93336',
        'version': 'wallet-v5.11.24',
        'X-Requested-With': 'wxapp',
        'x-wxa-page': 'pages/showsubs/order/confirm',
        'X-Channel-ID': '70001',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN',
        'Referer': 'https://servicewechat.com/wxdbb4c5f1b8ee7da1/1569/page-frame.html'
    }

    # 发起 GET 请求
    response = requests.get(url, params=params, headers=headers)
    my_contacts = response.json().get("data")
    # for contact in my_contacts:
    #     print(contact)

    return my_contacts


fetch_my_maoyan_contacts()
