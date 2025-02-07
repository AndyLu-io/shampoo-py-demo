import requests

# 设置请求头
headers = {
    "Host": "m.piaoxingqiu.com",
    "Connection": "keep-alive",
    "Content-Length": "105",
    "terminal-src": "WEIXIN_MINI",
    "content-type": "application/json",
    "src": "weixin_mini",
    "ver": "4.23.4",
    "access-token": "eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNp8UU9PwjAU_y49c2i7tuu8AbIwA84gi3BayvoGC7A2W1HU-N1tAY0nj32_v-_1Exl1crusrQ26-0TK2kyjO_R2VlpgrSWhkRI0ogkaoFPbmPYCm2K1FL3EXbZPdy_NQ2U_tNlSp1bzzBONhRsvS7Oc58vtdJ-uz3Zf7kZ182pqUjyu0Zd37KH7id40H2OjwavS6ayce5v-tBn9DgUVsZIYQFMiOaOxFDVhCfM8r1yYQyCNivVk4SdHVxXBOnTgEqSGBOOqpgkXUEck4lzgq_CXJrhmjFFZA65iz8aE8Q2vNqGm5-UWOuXMv1zlLd279UWIrwBdtVOtu67Xng6HAXqFrvcnvOBWda5xlxcSXghn23SwbI5BHkcsTmImJIvZAFUdKPcXIgTfoP69d3C8nWg8zMp1Vo5neXFfXk5RPhWL8XT4PCmfZsNlmi_m16S_Ed7f92zhEFa79gzf0qoQF95f3wAAAP__.LuNXA-FWl4ZDE8_69KGAcLxnlcHpzwwSGNp34041hI1NkCcUEXIuV2Licr5q5KVlYfiHcbmuSD-ghBcOdFig8Q-vxolI2knhDw_SQnzzqIzCfWJGvfc176jXqlCgCiRBIMCXE0uJl-ow4OWNivz5Emdyp0v0YlzQDndCubrxsFE",
    "merchant-id": "6267a80eed218542786f1494",
    "front-trace-id": "m4wyhdiki76obbr3ym",
    "Angry-dog": "ODRkNDVkZTJkOGEyNWIyMDkwOTM0YjYzZjc5Yzk3YWMyNjFmMTU2YjIwMzM2ZjU5MDA1MmI5MDYzZmYxYWU2ZTo0YzVmMjExODM5OTg2MTA3YWI0ZDQ5NjU3MTg3YzcyMTQzODVhOTFiYTVlNmYwMWMzZjVkYjNhYzRhZjExOGYxM2MzZjA0OWE1YTkxNzIwYmNmNzNjZmZmZmE5YmJhMmNmMWM0ZWQwZDhkMmZlNjZjMGQ0NzczODAxZTM3MjZkNjg0MGY4N2M4MzRhYTc5ZDZlNTU5MDZjYjIzZDMwYjI5ZDZjZWYxNDliNjY4MDM4MmM5Y2QwYmRjY2QxZDI3Nzk6MTczNDcxMTU0MjAyOA",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wxad60dd8123a62329/312/page-frame.html"
}

# 设置请求URL和参数
url = "https://m.piaoxingqiu.com/cyy_gatewayapi/trade/buyer/order/v3/order_list"
params = {
    "lang": "zh",
    "length": 10,
    "offset": 0,
    "orderStatusQuery": "TERMINATED"
}

# 设置请求体
data = {
    "src": "weixin_mini",
    "merchantId": "6267a80eed218542786f1494",
    "ver": "4.23.4",
    "appId": "wxad60dd8123a62329"
}

# 发送POST请求
response = requests.post(url, headers=headers, params=params, json=data)
my_order_list = response.json().get("data")
for order in my_order_list:
    print(order)

# 打印响应
print(f"状态码: {response.status_code}")
print(f"响应内容: {response.text}")
