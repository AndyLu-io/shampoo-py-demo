import requests

from crawel.charles.fenwandao.constants.performance_constant import PerformanceConstant

# 请求 URL
url = PerformanceConstant.HOST + "/member/member/bearer/app/list"

def get_my_contacts():
    # 请求头
    headers = {
        "Host": "api.livelab.com.cn",
        "Connection": "keep-alive",
        "platform-type": "%E7%BA%B7%E7%8E%A9%E5%B2%9B%E5%BE%AE%E4%BF%A1%E5%B0%8F%E7%A8%8B%E5%BA%8F",
        "content-type": "application/json",
        "x-fwd-anonymousId": "ocXac5EEdkqUv0EFIHnOzoMToVpY",
        "platform-version": "3.3.1",
        "Authorization": PerformanceConstant.AUTH_TOKEN,
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wx5a8f481d967649eb/103/page-frame.html",
    }

    # 发起 GET 请求
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查 HTTP 请求是否成功
        # 输出响应结果
        return response.json().get("data")
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")


my_contacts = get_my_contacts()
for my_contact in my_contacts:
    print(my_contact)