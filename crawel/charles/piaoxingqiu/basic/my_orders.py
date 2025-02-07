import requests

# 设置请求头
headers = {
    "Host": "m.piaoxingqiu.com",
    "Connection": "keep-alive",
    "terminal-src": "WEIXIN_MINI",
    "content-type": "application/json",
    "src": "weixin_mini",
    "ver": "4.23.4",
    "access-token": "eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNp8UU9PwjAU_y49c2i7tuu8AbIwA84gi3BayvoGC7A2W1HU-N1tAY0nj32_v-_1Exl1crusrQ26-0TK2kyjO_R2VlpgrSWhkRI0ogkaoFPbmPYCm2K1FL3EXbZPdy_NQ2U_tNlSp1bzzBONhRsvS7Oc58vtdJ-uz3Zf7kZ182pqUjyu0Zd37KH7id40H2OjwavS6ayce5v-tBn9DgUVsZIYQFMiOaOxFDVhCfM8r1yYQyCNivVk4SdHVxXBOnTgEqSGBOOqpgkXUEck4lzgq_CXJrhmjFFZA65iz8aE8Q2vNqGm5-UWOuXMv1zlLd279UWIrwBdtVOtu67Xng6HAXqFrvcnvOBWda5xlxcSXghn23SwbI5BHkcsTmImJIvZAFUdKPcXIgTfoP69d3C8nWg8zMp1Vo5neXFfXk5RPhWL8XT4PCmfZsNlmi_m16S_Ed7f92zhEFa79gzf0qoQF95f3wAAAP__.LuNXA-FWl4ZDE8_69KGAcLxnlcHpzwwSGNp34041hI1NkCcUEXIuV2Licr5q5KVlYfiHcbmuSD-ghBcOdFig8Q-vxolI2knhDw_SQnzzqIzCfWJGvfc176jXqlCgCiRBIMCXE0uJl-ow4OWNivz5Emdyp0v0YlzQDndCubrxsFE",
    "merchant-id": "6267a80eed218542786f1494",
    "front-trace-id": "m4wyaxy5g56l6qa2yyq",
    "Angry-dog": "YWRiZDQ3MTUxY2E3ODIxNjk3NmJmODQ3YzJlZGI1M2YyNjFmMTU2YjIwMzM2ZjU5MDA1MmI5MDYzZmYxYWU2ZTo5ODNhOGU4ODY3NmJmN2IyNzlkZTgxMjRiZTVmNjM1YzcxMDU2YmQ4ODhiYmJkMDU1MmMyOGM3ZDZlYzNjNGY4NzI4YjZiNmI0ZDk5MjA2ZjcxNWIwMjY1Y2JmYTE5M2M1MzFjNjk5MzVlYTBhZTNhMzMwOTQ0MDM5Y2FkMmI2YjczNmYxOWY4OWRiMzc4YjBkYjM1YjBjZjg3ZTUyNTc4YzBiYzJkNTZkYmVkMWYxODQwNTlkZDc3ZjI4MDljYjU6MTczNDcxMTA3MjU4OQ",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wxad60dd8123a62329/312/page-frame.html"
}

# 设置请求URL
url = "https://m.piaoxingqiu.com/cyy_gatewayapi/trade/buyer/order/v5/orders/676597e6158a5b00016550e5"
params = {
    "lang": "zh",
    "src": "weixin_mini",
    "merchantId": "6267a80eed218542786f1494",
    "ver": "4.23.4",
    "appId": "wxad60dd8123a62329",
    "fromPage": "ORDER_DETAIL_PAGE"
}

# 发送GET请求
response = requests.get(url, headers=headers, params=params)

# 打印响应
print(f"状态码: {response.status_code}")
print(f"响应内容: {response.text}")
