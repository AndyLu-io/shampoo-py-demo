import requests

# 请求的 URL 和查询参数
url = "https://m.piaoxingqiu.com/cyy_gatewayapi/home/pub/v5/citys/current_location"
params = {
    "lang": "zh",
    "src": "weixin_mini",
    "merchantId": "6267a80eed218542786f1494",
    "ver": "4.23.4",
    "appId": "wxad60dd8123a62329"
}

# 请求头
headers = {
    "Host": "m.piaoxingqiu.com",
    "Connection": "keep-alive",
    "terminal-src": "WEIXIN_MINI",
    "content-type": "application/json",
    "ver": "4.23.4",
    "access-token": "eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNp8UU9PwjAU_y49c-i6tivcYLowA84gi3BayvrmFsbabEVB43e3BTSePPb9_r7XT6Tl0dZpV2k0-UTSmFShCXo_ScWxUiIgoeQkJGM0Qseu0d0F1vlmzQeB-3Sf1C_NQ2k-lH4lVm6WqSNqAzdemqQZy9av832yPZl9Uc-q5k1XQf64RV_OcYD-J3rXfMRagVMl80WxdDbDcTf7HXLCIykwgCKBYJREglcBHVPHc8qVbj1plm_vV25ysGXurX0HJkAoGGNcVmTMOFRhEDLG8VX4S-NMUUqJqACXkWPjgLIdK3e-puNlBnpp9b9c6Szt2bgigasAfVnLzl7X645tO0Jv0A_uhBfcyN429vJC3AnhZJoe1s3By6OQChpxzCgjI1T2IO0fKOIBuUHDebBwuJ0onqbFNi3iRZbfFZdTFE_5Kp5Pn--Lp8V0nWSr5TXpb4Tzdz07aP1q157-Wzrp4_z76xsAAP__.QPQR7S-kFruR0l0TQGXyyos1vcbOMrg73gxCztRqRMFm6fjbtxnjubWO877jPjWbdwdu0PUtf8KEK858WWC-_RXHQaHgXdt_wbQDuTpkrly1wYvItJqEApfeKTdkEv1Z28a2HhS0R4nB9ThB8y0EHGbOQScHyJHgM4yDQLT3QXc",
    "front-trace-id": "m4xteqtmwknp53g3pz",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN",
    "Referer": "https://servicewechat.com/wxad60dd8123a62329/312/page-frame.html"
}

# 发起请求
response = requests.get(url, params=params, headers=headers)

# 输出请求的完整 URL 和返回结果
print("完整请求 URL:", response.url)
print("返回状态码:", response.status_code)
print("返回内容:", response.text)

data = response.json().get("data")

print(
    data
)
