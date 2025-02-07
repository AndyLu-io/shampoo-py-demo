from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from contants import Constant

# 设置请求头
headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'company': '202401301442345769',
    'origin': 'https://www.gwzx.vip',
    'platformid': '202401301442345769',
    'priority': 'u=1, i',
    'referer': 'https://www.gwzx.vip/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'token': '31ae4d76c08f4c0d926fb2652ca0ee62',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}


# 发送请求的函数
def send_request():
    url = Constant.BASE_URL + "/supplier/workbench/rank/merchant"
    response = requests.get(url, headers=headers)
    return response


# 使用线程池来并发请求 10 次
def make_concurrent_requests():
    with ThreadPoolExecutor(max_workers=100) as executor:
        # 提交 10 个并发请求
        futures = [executor.submit(send_request) for _ in range(1000)]

        # 按照完成顺序获取结果
        for future in as_completed(futures):
            try:
                response = future.result()
                if response.status_code == 200:
                    print("请求成功")
                    print(response.text)
                    data = response.json().get('data')
                    print(data[0])
                else:
                    print(f"请求失败，状态码: {response.status_code}")
            except Exception as e:
                print(f"请求发生错误: {e}")


if __name__ == "__main__":
    make_concurrent_requests()
# # 检查响应状态
# if response.status_code == 200:
#     print("请求成功:")
#     print(response.text)
#     data=response.json().get('data')
#     print(data[0])
# else:
#     print(f"请求失败，状态码: {response.status_code}")
