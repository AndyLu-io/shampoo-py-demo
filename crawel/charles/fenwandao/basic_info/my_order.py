import requests

from crawel.charles.fenwandao.constants.performance_constant import PerformanceConstant

# 请求的基本信息
url = PerformanceConstant.HOST + "/performance/app/order/list"


def get_my_orders():
    params = {
        "pageNum": 1,
        "pageSize": 100,
        "type": 0,
    }

    # 请求头
    headers = {
        "Host": "api.livelab.com.cn",
        "Connection": "keep-alive",
        "X-REQUEST-STARTTIME": "1734675152845",
        "platform-type": "%E7%BA%B7%E7%8E%A9%E5%B2%9B%E5%BE%AE%E4%BF%A1%E5%B0%8F%E7%A8%8B%E5%BA%8F",
        "content-type": "application/json",
        "x-fwd-anonymousId": "ocXac5EEdkqUv0EFIHnOzoMToVpY",
        "platform-version": "3.3.1",
        "Authorization": PerformanceConstant.AUTH_TOKEN,
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx5a8f481d967649eb/103/page-frame.html",
    }

    # headers["Authorization"] = "Bearer <新的Token>"

    # 发起 GET 请求
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # 如果发生HTTP错误，将抛出异常
        # 解析并打印响应结果
        return response.json().get("data").get("rows")
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")


orders = get_my_orders()
for order in orders:
    print(order)
