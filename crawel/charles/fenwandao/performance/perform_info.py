import requests

from crawel.charles.fenwandao.constants.performance_constant import PerformanceConstant

# 请求的 URL
url = PerformanceConstant.HOST + '/performance/app/project/get_performs'


def get_performance_info(project_id):
    # 请求的参数
    params = {
        'project_id': project_id,
        'v': '1734678000',
        'retry': 'false'
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
        print("请求成功:", response.text)  # 打印响应内容（假设是 JSON 格式）
        return response.json().get("data")
    else:
        print("请求失败，状态码:", response.status_code)


def get_performance_list(project_id):
    performance_info = get_performance_info(project_id)
    performInfos = performance_info['performInfos']
    for performInfo in performInfos:
        print(performInfo)
    return performInfos


def get_seat_plans(project_id):
    result_plans = []
    performInfos = get_performance_list(project_id)
    for performInfo in performInfos:
        date = performInfo['dateStr']
        perform = performInfo['performInfo'][0]
        seatPlans = perform['seatPlans']
        result_plans.append({
            'date': date,
            'seatPlans': seatPlans
        })

    return result_plans


result_plans = get_seat_plans('5141624343')
for result_plan in result_plans:
    print(result_plan)

# get_performance_list('8362414781')
