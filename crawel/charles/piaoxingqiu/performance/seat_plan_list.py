import requests

def fetch_seat_plan_list(show_id, session_id):
    # 请求的 URL 和查询参数
    url = f"https://m.piaoxingqiu.com/cyy_gatewayapi/show/pub/v5/show/{show_id}/session/{session_id}/seat_plans"
    params = {
        "lang": "zh",
        "src": "weixin_mini",
        "merchantId": "6267a80eed218542786f1494",
        "ver": "4.23.4",
        "appId": "wxad60dd8123a62329",
        "source": "FROM_QUICK_ORDER"
    }

    # 请求头
    headers = {
        "Host": "m.piaoxingqiu.com",
        "Connection": "keep-alive",
        "terminal-src": "WEIXIN_MINI",
        "content-type": "application/json",
        "src": "weixin_mini",
        "ver": "4.23.4",
        "access-token": "eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNp8UUtzgjAQ_i85e4CQhOBNrYx0tDhWpnpiIlmUUUkGovUx_e9N1Dqeesx-z91ckRIHs0nqUqHuFQmtE4m66PskJPOk5D4OBMMBjlAHHepK1TdYZYs5a7nXJNt481W9F_oi1RobsZgklqg0PHhJnKQ0na9H23h50tt80y-royr97GOJfqxjC81f9Kq6DJQEq4pH43xibdrDqv8cMsxCwT0AiX1OCQ45K30SEcuzypnaOVI_Ww5ndrI3ReasXQfKgUuIPK8ocUQZlIEfUMq8u_BJY1QSQjAvwStCy_Z8Qle0WLmalpdqaIRR_3KFtTRnbYv4tgI0xUbU5r5efdjtOugITWtPeMO1aExlbi_ErBBOumpgXu2dPAwIJ1GEfYrDDioaEOYFCllAH1B7bg3sHyca9JJ8meSDcZq95bdT5NNsNhj1Pof5dNybx-lsck96jbD-tmcNO7favaf7llq4OPf--QUAAP__.TcmePVaveR6KLc6mfZfzYaIwpfOWTCmCk5JCkq1V6hAcZgT5xEoQM9ReiJQPT_A3b6pD4E59n4m81TUZOprpSXfZ94ybPGvhR3EXUxXu7E3T9X0HxFbYrW0tXLyQUihLOXUzsJX1bc0S2a5Iynu4NvoHsUlOPz_7vqKNIDscN2w",
        "merchant-id": "6267a80eed218542786f1494",
        "front-trace-id": "m4xtv9ey7yaeoppznz5",
        "Angry-dog": "MWQxMjgyYmYzMDIyNWVjNzAzMGU5MGFmYTczYzZjZDMyNjFmMTU2YjIwMzM2ZjU5MDA1MmI5MDYzZmYxYWU2ZTo0ODFjM2FmYWVkNmIyMWY3ZWVjMzBiYmFlYzRmYzQ4Mzc4NGYzNWQ1ZmNmODJkMzIzNDkxMzE5OGQ0Y2M2MDdiM2NiOGM3NDJlNjExNWEyOGMzYjBjMmE2ZGQ4NTJkNDFkNWU5ZWM3MmU5NWU0Zjc1ZjE2YTJiM2VkMDdmODA4MGZmOGRjZDk3MzNlNWQwNjgxMjU1MjM3YmI0OGIyOTA3YTU2YWU5ZGY5ODY2M2ZiNDM4NzYzNzYyZjA0MzM3N2M6MTczNDc2Mzg2NTc1NQ",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxad60dd8123a62329/312/page-frame.html"
    }

    # 发起请求
    response = requests.get(url, params=params, headers=headers)

    seatPlans = response.json().get('data').get('seatPlans')

    return seatPlans

    # 输出请求结果
    # print("完整请求 URL:", response.url)
    # print("返回状态码:", response.status_code)
    # print("返回内容:", response.text)


seatPlans = fetch_seat_plan_list('67d6dc4499c2e800011bfa0f', '67d6dcd982f5d6000104950b')
for seatPlan in seatPlans:
    print(seatPlan['seatPlanId'])
    print(seatPlan)

