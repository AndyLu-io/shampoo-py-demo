import requests

from crawel.charles.fenwandao.constants.performance_constant import PerformanceConstant
from crawel.charles.fenwandao.performance.perform_info import get_seat_plans

# 请求的 URL
url = PerformanceConstant.HOST + '/performance/app/project/seatPlanStatus'


def get_seat_plan_status(seatPlanIds):
    # 查询参数
    params = {
        'seatPlanIds': seatPlanIds,
        'type': '3'
    }

    # 请求头
    headers = {
        'Host': 'api.livelab.com.cn',
        'Connection': 'keep-alive',
        'platform-type': '%E7%BA%B7%E7%8E%A9%E5%B2%9B%E5%BE%AE%E4%BF%A1%E5%B0%8F%E7%A8%8B%E5%BA%8F',
        'content-type': 'application/json',
        'x-fwd-anonymousId': 'ocXac5EEdkqUv0EFIHnOzoMToVpY',
        'platform-version': '3.3.1',
        'Authorization': PerformanceConstant.AUTH_TOKEN,
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN',
        'Referer': 'https://servicewechat.com/wx5a8f481d967649eb/103/page-frame.html'
    }

    # 发起 GET 请求
    response = requests.get(url, headers=headers, params=params)

    # 输出响应内容
    if response.status_code == 200:
        print("请求成功:", response.json())  # 假设响应内容为 JSON 格式
        return response.json().get("data")

    else:
        print(f"请求失败，状态码: {response.status_code}, 响应内容: {response.text}")


seat_plan_maps = get_seat_plans('6258744554')
for seat_plan_map in seat_plan_maps:
    date = seat_plan_map['date']
    seat_plan_ids = [seat_plan['seatPlanId'] for seat_plan in seat_plan_map['seatPlans']]
    seat_plan_status_list = get_seat_plan_status(seat_plan_ids)
    for seat_plan_status in seat_plan_status_list:
        print('date:'+ date)
        print(seat_plan_status)