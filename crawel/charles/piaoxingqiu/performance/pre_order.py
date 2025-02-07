import requests

from crawel.charles.piaoxingqiu.constants.id_util import generate_order_number
from crawel.charles.piaoxingqiu.constants.piao_contants import PiaoConstans
from crawel.charles.piaoxingqiu.performance.seat_plan_list import fetch_seat_plan_list


# def get_price(seat_plan_list, sku_id):
#     for seat_plan in seat_plan_list:
#         if seat_plan.get("skuId") == sku_id:
#             return seat_plan.get("originalPrice")


def build_ticketItems(num):
    result_item_list = []
    for i in range(0, num):
        result_item_list.append(
            {
                "id": generate_order_number(),
            }
        )
    return result_item_list


def build_data(show_id, session_id, can_buy_seat_plan, num):
    data = {
        "src": "weixin_mini",
        "merchantId": PiaoConstans.MERCHANT_ID,
        "ver": "4.23.4",
        "appId": PiaoConstans.APP_ID,
        "priorityId": "",
        "items": [
            {
                "sku": {
                    "skuId": can_buy_seat_plan['seatPlanId'],
                    "skuType": "SINGLE",
                    "ticketPrice": can_buy_seat_plan['originalPrice'],
                    "qty": num,
                    "ticketItems": build_ticketItems(num)
                },
                "spu": {
                    "showId": show_id,
                    "sessionId": session_id,
                }
            }
        ],
        "orderSource": "COMMON"
    }
    return data


def get_can_buy_seat_plan(seat_plan_list):
    for seat_plan in seat_plan_list:
        if seat_plan.get("canBuyCount") > 0:
            return seat_plan
    return None


def handle_pre_order(show_id, session_id, num):
    # 请求的 URL
    url = "https://m.piaoxingqiu.com/cyy_gatewayapi/trade/buyer/order/v5/pre_order"
    params = {
        "lang": "zh"
    }

    # 请求头
    headers = {
        "Host": PiaoConstans.HOST,
        "Connection": "keep-alive",
        "Content-Length": "375",
        "terminal-src": "WEIXIN_MINI",
        "content-type": "application/json",
        "src": "weixin_mini",
        "ver": "4.23.4",
        "access-token": PiaoConstans.AUTH_TOKEN,
        "merchant-id": PiaoConstans.MERCHANT_ID,
        "front-trace-id": "m4xu9ukp7p6vdkl7rfn",
        "Angry-dog": PiaoConstans.ANGRY_DOG,
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxad60dd8123a62329/312/page-frame.html"
    }
    seat_plan_list = fetch_seat_plan_list(show_id, session_id)

    can_buy_seat_plan = get_can_buy_seat_plan(seat_plan_list)
    # 请求体
    data = build_data(show_id, session_id, can_buy_seat_plan, num)

    # 发起 POST 请求
    response = requests.post(url, params=params, headers=headers, json=data)
    print("返回内容:", response.text)
    statusCode =response.json().get("statusCode")
    if statusCode == 200:
        supportDeliveries = response.json().get("data").get("supportDeliveries")
        return data, supportDeliveries
    else:
        print("请求失败")
        return None, None


    # audiences = response.json().get("data").get("audiences")
    #
    # identity = response.json().get("data").get("identityVO")

    # 输出请求结果
    # print("返回状态码:", response.status_code)
    # for audience in audiences:
    #     print(audience)
    #
    # print(identity)
    #
    # for supportDelivey in supportDeliveries:
    #     print(supportDelivey)


    # handle_pre_order('672c83e5077b340001a8744a', '672c83e5077b340001a87456')


# seat_plan_list = fetch_seat_plan_list('672c83e5077b340001a8744a', '672c83e5077b340001a87456')
# seatPlanId = seat_plan_list[0]['seatPlanId']
# print(seatPlanId)
# # print(seat_plan)
# can_buy_seat_plan = get_can_buy_seat_plan(seat_plan_list)
# build_data = build_data('672c83e5077b340001a8744a', '672c83e5077b340001a87456', can_buy_seat_plan, 1)
# print(build_data)


# handle_pre_order('672c83e5077b340001a8744a', '672c83e5077b340001a87456', 1)
