import requests
# 发送 GET 请求
url = 'https://m.piaoxingqiu.com/cyy_gatewayapi/user/buyer/v3/user_audiences'

# 定义请求头和请求参数
headers = {
    'Host': 'm.piaoxingqiu.com',
    'Connection': 'keep-alive',
    'terminal-src': 'WEIXIN_MINI',
    'content-type': 'application/json',
    'src': 'weixin_mini',
    'ver': '4.23.4',
    'access-token': 'eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNp8UUtzgjAQ_i85e4CQhOBNrYx0tDhWpnpiIlmUUUkGovUx_e9N1Dqeesx-z91ckRIHs0nqUqHuFQmtE4m66PskJPOk5D4OBMMBjlAHHepK1TdYZYs5a7nXJNt481W9F_oi1RobsZgklqg0PHhJnKQ0na9H23h50tt80y-royr97GOJfqxjC81f9Kq6DJQEq4pH43xibdrDqv8cMsxCwT0AiX1OCQ45K30SEcuzypnaOVI_Ww5ndrI3ReasXQfKgUuIPK8ocUQZlIEfUMq8u_BJY1QSQjAvwStCy_Z8Qle0WLmalpdqaIRR_3KFtTRnbYv4tgI0xUbU5r5efdjtOugITWtPeMO1aExlbi_ErBBOumpgXu2dPAxIGDIcRpSQDioaEOYFYjziD6g9twb2jxMNekm-TPLBOM3e8tsp8mk2G4x6n8N8Ou7N43Q2uSe9Rlh_27OGnVvt3tN9Sy1cnHv__AIAAP__.PN14_GYjEKavIibd9BDVTdfFylgNuPhCc8gI76K1CF-299SlZ1BM6dDakU6URVLfMBEiiKRKv0Aahphl5KmFJpTJLGKPNLa9jqIZwen9LsUMlhh7vHohV9l-2FXVHZgSlREPKRQQMb12WzTjnRf0CPMx-i8UDZ0Dy8DBDZsltK8',
    'merchant-id': '6267a80eed218542786f1494',
    'front-trace-id': 'm4wls1n832z3gdy9edq',
    'Angry-dog': 'MGI0NTBkYmJjMzYyYjY1ZmRhZjJlOWRjZWMxMmJjOWEyNjFmMTU2YjIwMzM2ZjU5MDA1MmI5MDYzZmYxYWU2ZToyYjU0NGIxY2QzZWU2ZjhkYTgwY2E0ZDM4MGJhNzAxYzRkMjdmODE3ODM3NzM1ZGQ2ZWFkMGViMTE3OTRkMjkwNTM4MTFhMjRlNmMxZjJmMzYwZTc5MDk1MDUzYjNlYmNjMjZiMmQ4MzJhYjQ4OTZmOWY0ZWUzN2FjMDQ3YzZiNzc4ZTBmYTQ1MDk2NzZjMjA0M2NhYzE2MjVkNjcyOWU5OWFjOWMwM2YyMGM3NDNjNWMzMjYyZTYxYjUxOWUyZDM6MTczNDY4OTg4Mjk2MA',
    'Accept-Encoding': 'gzip,compress,br,deflate',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN',
    'Referer': 'https://servicewechat.com/wxad60dd8123a62329/312/page-frame.html'
}

# 定义请求参数
params = {
    'idTypes': '',
    'lang': 'zh',
    'length': '500',
    'offset': '0',
    'showId': '',
    'src': 'weixin_mini',
    'merchantId': '6267a80eed218542786f1494',
    'ver': '4.23.4',
    'appId': 'wxad60dd8123a62329'
}


response = requests.get(url, headers=headers, params=params)

# 检查响应
if response.status_code == 200:
    data = response.json()
    print("响应数据:", data)
else:
    print(f"请求失败，状态码: {response.status_code}, 错误信息: {response.text}")
