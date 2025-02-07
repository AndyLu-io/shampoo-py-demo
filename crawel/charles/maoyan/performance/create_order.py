import requests
import json

from crawel.charles.maoyan.constants.maoyan_constants import MaoYanConstants

# URL for the POST request
url = "https://wx.maoyan.com/maoyansh/myshow/ajax/tx/order/create"


def handle_create_order(projectId, showId, ticketId, price, num, watch_contacts_str):
    total_price = price * num

    # Headers for the request
    headers = {
        'Host': MaoYanConstants.HOST,
        "Connection": "keep-alive",
        "Content-Length": "6080",
        "x-wxa-query": "%7B%22performance_id%22%3A%22366138%22%7D",
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

    # Data for the POST request (ensure this is in the correct JSON format as per your requirements)
    data = {
        "recipientMobile": "15757174039",
        "recipientName": "卢晓波",
        "recipientIdNo": "",
        "recipientMobileAreaCode": "86",
        "dpCityId": 50,
        "salesPlanId": ticketId,
        "tpId": 3927,
        "salesPlanSellPrice": f"{price}",
        "salesPlanCount": num,
        "totalPrice": f"{total_price}",
        "fetchTicketWayId": 6316978,
        "recipientAddressId": 0,
        "performanceId": projectId,
        "txDeviceToken": "v2:xakBLRRjLakq4nCycfb5JjykIL/AsIi1Adptcz91ShaB2NDXqy8Je5gtBZXOXVvhbzOYao430PwBWnkelUDnBnr18dGPE0qjo0PSGw1/8Td6NEwtjh8zVSDlfJYRLT8SRptrrUUQmDqP8XXLjYe9gtieBo7EIZhIm2M6e8lXEDccvZzeyAOFQnUIZE+yJaKB4gc2EfTIwUL/H1T/S1m2dyd8Cp+UWy7DIEIwkWgWXKCH7SWhFzvN6lKYouVBnpAgvXWkvOv62GUda3FC7e4BFozW8gMDFy69V5M2bYJ60ZUJFGo=",
        "showId": showId,
        "activityUser": False,
        "scene": 1106,
        "riskRequest": {
            "version": "1.0.0",
            "fingerprint": "WX__ver1.2.0_CCCC_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",
            "wxAppId": "wxdbb4c5f1b8ee7da1"
        },
        "wxOpenId": "o31Py0CqF0okNBr5-RDHU9zPqpj8",
        "realNameRequest": {
            "needRealName": True,
            "realNameUserVOList": watch_contacts_str
        },
        "accountType": -1
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Print the response (status code and content)
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
