import requests

from crawel.charles.piaoxingqiu.constants.piao_contants import PiaoConstans

# 请求的 URL
url = "https://m.piaoxingqiu.com/cyy_gatewayapi/trade/buyer/order/v5/create_order"


def build_payment_param(data, default_audience_list):
    items = data['items']
    sku = items[0]['sku']
    num = len(default_audience_list)
    amount = sku['ticketPrice'] * num
    return {
        "totalAmount": f"{amount}",
        "payAmount": f"{amount}",
    }


#     for item in items:
#         item['sku'] = build_sku_info(item['sku'])


def build_ticket_item(ticketItem, default_audience):
    return {
        "id": ticketItem['id'],
        "audienceId": default_audience
    }


def build_ticket_items(sku_data, default_audience_list):
    result_item_list = []
    ticketItems = sku_data['ticketItems']
    num = len(default_audience_list)
    for i in range(0, num):
        result_item = build_ticket_item(ticketItems[i], default_audience_list[i])
        result_item_list.append(result_item)
    return result_item_list


def build_sku_info(sku_data, default_audience_list):
    sku = {
        "skuId": sku_data['skuId'],
        "skuType": sku_data['skuType'],
        "ticketPrice": sku_data['ticketPrice'],
        "qty": len(default_audience_list),
        "ticketItems": build_ticket_items(sku_data, default_audience_list)
    }
    return sku


def get_support_method(supportDeliveries):
    return supportDeliveries[0]['name']


def build_price_item(data, default_audience_list):
    items = data['items']
    sku = items[0]['sku']
    num = len(default_audience_list)
    amount = sku['ticketPrice'] * num
    return {
        "applyTickets": [

        ],
        "priceItemName": "票款总额",
        "priceItemVal": f"{amount}",
        "priceItemType": "TICKET_FEE",
        "priceItemSpecies": "SEAT_PLAN",
        "direction": "INCREASE",
        "priceDisplay": f"￥{amount}"
    }


def handle_create_order(show_id, session_id, origin_data, default_audience_list, supportDeliveries):
    items = origin_data['items']
    sku_data = items[0]['sku']
    params = {
        "lang": "zh"
    }

    # 请求头
    headers = {
        "Host": PiaoConstans.HOST,
        "Connection": "keep-alive",
        "Content-Length": "931",
        "terminal-src": "WEIXIN_MINI",
        "content-type": "application/json",
        "src": "weixin_mini",
        "ver": "4.23.4",
        "access-token": PiaoConstans.AUTH_TOKEN,
        "merchant-id": PiaoConstans.MERCHANT_ID,
        "front-trace-id": "m4xuamh785h9xj2hm53",
        "Angry-dog": PiaoConstans.ANGRY_DOG,
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxad60dd8123a62329/312/page-frame.html"
    }

    # 请求体
    data = {
        "src": "weixin_mini",
        "merchantId": PiaoConstans.MERCHANT_ID,
        "ver": "4.23.4",
        "appId": PiaoConstans.APP_ID,
        "addressParam": {

        },
        "locationParam": {
            "locationCityId": "BL1120",
            "bsCityId": "BL1120"
        },
        "paymentParam": build_payment_param(origin_data, default_audience_list),
        "priceItemParam": [
            build_price_item(origin_data, default_audience_list)
        ],
        "items": [
            {
                "sku": build_sku_info(sku_data, default_audience_list),
                "spu": {
                    "showId": show_id,
                    "sessionId": session_id,
                    "promotionVersionHash": "EMPTY_PROMOTION_HASH",
                    "addPromoVersionHash": "EMPTY_PROMOTION_HASH"
                },
                "deliverMethod": get_support_method(supportDeliveries)
            }
        ],
        "priorityId": "",
        "addPurchasePromotionId": "",
        "many2OneAudience": {

        },
        "orderSource": "COMMON"
    }

    print(data)
    # 发起 POST 请求
    response = requests.post(url, params=params, headers=headers, json=data)

    # 输出请求结果
    print("返回状态码:", response.status_code)
    print("返回内容:", response.text)
