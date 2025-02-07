import requests

# 请求 URL
url = "https://api.livelab.com.cn/auth/applet/wx/v3/getWxAuthInfo"

# 查询参数
params = {
    "jscode": "0e1xB9100z4tnT1mlj30042l4Y2xB91E",
    "blackBox": ""
}

# 请求头
headers = {
    "Host": "api.livelab.com.cn",
    "Connection": "keep-alive",
    "platform-type": "%E7%BA%B7%E7%8E%A9%E5%B2%9B%E5%BE%AE%E4%BF%A1%E5%B0%8F%E7%A8%8B%E5%BA%8F",
    "content-type": "application/x-www-form-urlencoded;charset=utf-8",
    "x-fwd-anonymousId": "1734675220173-3017318-09e781948b0fcd8-22397867",
    "platform-version": "3.3.1",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wx5a8f481d967649eb/103/page-frame.html",
}

# 发起 GET 请求
try:
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # 检查 HTTP 请求是否成功
    # 输出响应结果
    print("请求成功，响应结果：")
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
