import requests

from crawel.charles.maoyan.constants.maoyan_constants import MaoYanConstants

# 请求 URL
url = 'https://wx.maoyan.com/my/odea/show/tickets'

def fetch_ticket_list(projectId, showId):
    # 请求头部信息
    headers = {
        'Host': MaoYanConstants.HOST,
        'Connection': 'keep-alive',
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

    # 请求参数
    params = {
        'token': 'MY_700t8KrQYFhKaD55-fp7yPb64soAAAAwv66FKiPpe2w_bF1BreKnhbPQBcbYE53te7KqYZ15mDH-_aXWL7lg1_p--6g3gzoJAAAAqwAAAAEB',
        'sellChannel': '7',
        'showId': showId,
        'projectId': projectId,
        'clientPlatform': '2',
        'cityId': '50'
    }

    # 发送 GET 请求
    response = requests.get(url, headers=headers, params=params)

    # 打印响应内容
    if response.status_code == 200:
        ticket_list = response.json().get('data').get('ticketsVO')
        for ticket in ticket_list:
            remainingStock = ticket['remainingStock']
            ticketPriceVO = ticket['ticketPriceVO']
            if remainingStock > 0:
                print(f"票价: {ticketPriceVO['ticketPrice']}, 库存: {remainingStock}")
                print(ticket)
    else:
        print(f"请求失败，状态码: {response.status_code}")



fetch_ticket_list(366138,2284212)


