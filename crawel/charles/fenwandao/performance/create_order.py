import requests
import time
from datetime import datetime

from crawel.charles.fenwandao.constants.performance_constant import PerformanceConstant
from crawel.charles.fenwandao.performance.perform_info import get_seat_plans

# 请求的 URL
url = 'https://api.livelab.com.cn/order/app/center/v3/create'
my_friends = [11166406]


def handle_commit_order(projectId, performId, frequentIds, seatPlanIds):
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

    # POST 请求的 JSON 数据
    payload = build_payload_data(projectId, performId, frequentIds, seatPlanIds)

    # 发送 POST 请求
    response = requests.post(url, headers=headers, json=payload)

    # 输出响应内容
    if response.status_code == 200:
        print("请求成功:", response.json())  # 假设响应内容为 JSON 格式
    else:
        print(f"请求失败，状态码: {response.status_code}, 响应内容: {response.text}")


def build_payload_data(projectId, performId, frequentIds, seatPlanIds):
    payload = {
        "deliveryType": 1,
        "contactName": "卢晓波",
        "contactPhone": "15757174039",
        "combineTicketVos": None,
        "ordinaryTicketVos": None,
        "payment": 1,
        "totalPrice": 1,
        "performId": performId,
        "projectId": projectId,
        "privilegeCodeList": [],
        "audienceCount": 1,
        "frequentIds": frequentIds,
        "seatPlanIds": seatPlanIds,
        "blackBox": ":0"
    }

    return payload


def crete_order(projectId):
    result_plans = get_seat_plans(projectId)
    result_plan = result_plans[len(result_plans) - 1]
    seatPlan = result_plan['seatPlans'][0]
    seatPlanId = seatPlan['seatPlanId']
    performId = seatPlan['performId']
    handle_commit_order(projectId, performId, my_friends, [seatPlanId])


def crete_order_with_time(project_id, specific_time_str):
    specific_time = datetime.strptime(specific_time_str, "%Y-%m-%d %H:%M:%S")

    # 等待直到当前时间大于特定时间
    print(f"等待时间到达 {specific_time_str} ...")
    while datetime.now() < specific_time:
        time.sleep(0.01)  # 每秒检查一次

    print(f"时间已到达 {specific_time_str}，开始执行下单请求...")

    crete_order(project_id)


project_id = '7648781775'
# 定义特定时间（这里以字符串形式给出，格式：YYYY-MM-DD HH:MM:SS）
specific_time_str = "2024-12-20 16:55:00"

# crete_order_with_time(project_id, specific_time_str)

crete_order(project_id)
