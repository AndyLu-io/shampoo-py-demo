import requests

from crawel.charles.maoyan.constants.maoyan_constants import MaoYanConstants

# 设置请求URL和参数
url = "https://wx.maoyan.com/my/odea/project/detail"

def fetcha_project_detail(projectId):
    # 设置请求头
    headers = {
        'Host': MaoYanConstants.HOST,
        "Connection": "keep-alive",
        "content-type": "application/json",
        "x-wxa-query": "%7B%22id%22%3A%22370356%22%2C%22isNewPage%22%3A%22true%22%2C%22performance_id%22%3A%22370356%22%2C%22myyc_source%22%3A%22%22%7D",
        "x-wxa-referer": "pages/show/index/index",
        "uuid": "61232c078af99235d38b24c687b93336",
        "version": "wallet-v5.11.24",
        "X-Requested-With": "wxapp",
        "x-wxa-page": "pages/show/detail/v2/index",
        "X-Channel-ID": "70001",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2c) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxdbb4c5f1b8ee7da1/1569/page-frame.html"
    }

    params = {
        "detailType": 1,
        "poi": "false",
        "buyInstructionType": 1,
        "sellChannel": 7,
        "cityId": 50,
        "projectId": projectId,
        "token": "MY_700t8KrQYFhKaD55-fp7yPb64soAAAAwv66FKiPpe2w_bF1BreKnhbPQBcbYE53te7KqYZ15mDH-_aXWL7lg1_p--6g3gzoJAAAAqwAAAAEB",
        "decorateShowType": 2,
        "clientPlatform": 2
    }

    # 发送GET请求
    response = requests.get(url, headers=headers, params=params)

    # 打印响应
    print(f"状态码: {response.status_code}")
    print(f"响应内容: {response.text}")


fetcha_project_detail(362043)