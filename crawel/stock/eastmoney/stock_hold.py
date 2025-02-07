import requests
from urllib.parse import urlencode

from crawel.stock.db.dao.institutional_holdings_dao import InstitutionalHoldingsDAO

base_url = 'https://data.eastmoney.com/dataapi/zlsj/list'


def fetch_data(date, type, zjc, sort_field, sort_direc, page_num, page_size):
    # 基础 URL

    # 动态构建 URL 参数
    params = {
        'date': date,  # 日期
        'type': type,  # 类型
        'zjc': zjc,  # 证券简称
        'sortField': sort_field,  # 排序字段
        'sortDirec': sort_direc,  # 排序方向
        'pageNum': page_num,  # 页码
        'pageSize': page_size  # 每页大小
    }

    # 使用 urlencode 构建查询字符串
    query_string = urlencode(params)
    url = f"{base_url}?{query_string}"

    # 请求头
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'qgqp_b_id=bbf3d2421b499d43435ce01c0368cd05; st_si=30929231181545; qRecords=%5B%7B%22name%22%3A%22%u4E2D%u56FD%u4EA4%u5EFA%22%2C%22code%22%3A%22SH601800%22%7D%5D; st_asi=delete; HAList=ty-0-300059-%u4E1C%u65B9%u8D22%u5BCC%2Cty-0-300750-%u5B81%u5FB7%u65F6%u4EE3; st_pvi=21614989227983; st_sp=2024-12-19%2011%3A27%3A40; st_inirUrl=https%3A%2F%2Fdata.eastmoney.com%2Fzlsj%2F; st_sn=54; st_psi=20241219171039487-113300300982-2239417023',
        'Referer': 'https://data.eastmoney.com/zlsj/2024-09-30-1-2.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }

    # 发起 GET 请求
    response = requests.get(url, headers=headers)

    # 检查请求是否成功
    if response.status_code == 200:
        # 打印返回的 JSON 数据
        stock_data_list = response.json().get('data', [])
        pages = response.json().get('pages')
        for stock_data in stock_data_list:
            save_stock_hold_data(stock_data)
        return pages

    else:
        print(f"请求失败，状态码: {response.status_code}")
        return None


def get_pages(params):
    # 动态构建 URL 参数

    # 使用 urlencode 构建查询字符串
    query_string = urlencode(params)
    url = f"{base_url}?{query_string}"

    # 请求头
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'qgqp_b_id=bbf3d2421b499d43435ce01c0368cd05; st_si=30929231181545; qRecords=%5B%7B%22name%22%3A%22%u4E2D%u56FD%u4EA4%u5EFA%22%2C%22code%22%3A%22SH601800%22%7D%5D; st_asi=delete; HAList=ty-0-300059-%u4E1C%u65B9%u8D22%u5BCC%2Cty-0-300750-%u5B81%u5FB7%u65F6%u4EE3; st_pvi=21614989227983; st_sp=2024-12-19%2011%3A27%3A40; st_inirUrl=https%3A%2F%2Fdata.eastmoney.com%2Fzlsj%2F; st_sn=54; st_psi=20241219171039487-113300300982-2239417023',
        'Referer': 'https://data.eastmoney.com/zlsj/2024-09-30-1-2.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }

    # 发起 GET 请求
    response = requests.get(url, headers=headers)

    # 检查请求是否成功
    if response.status_code == 200:
        # 打印返回的 JSON 数据
        try:
            pages = response.json().get('pages')
            return pages
        except Exception as e:
            print(f"解析失败: {e}")

    else:
        print(f"请求失败，状态码: {response.status_code}")
        return None


def save_stock_hold_data(stock_data):
    stock_hold_data = {
        "security_inner_code": stock_data.get("SECURITY_INNER_CODE"),
        "security_name_abbr": stock_data.get("SECURITY_NAME_ABBR"),
        "report_date": stock_data.get("REPORT_DATE"),
        "org_type": stock_data.get("ORG_TYPE"),
        "hould_num": stock_data.get("HOULD_NUM"),
        "total_shares": stock_data.get("TOTAL_SHARES"),
        "hold_value": stock_data.get("HOLD_VALUE"),
        "freeshares_ratio": stock_data.get("FREESHARES_RATIO"),
        "holdcha": stock_data.get("HOLDCHA"),
        "holdcha_num": stock_data.get("HOLDCHA_NUM"),
        "holdcha_ratio": stock_data.get("HOLDCHA_RATIO"),
        "secu_code": stock_data.get("SECU_CODE"),
        "totalshares_ratio": stock_data.get("TOTALSHARES_RATIO"),
        "org_type_name": stock_data.get("ORG_TYPE_NAME"),
        "qchange_rate": stock_data.get("QCHANGE_RATE"),
        "free_market_cap": stock_data.get("FREE_MARKET_CAP"),
        "free_shares": stock_data.get("FREE_SHARES"),
        "security_type_code": stock_data.get("SECURITY_TYPE_CODE"),
        "holdcha_value": stock_data.get("HOLDCHA_VALUE"),
        "security_code": stock_data.get("SECURITY_CODE"),
        "freeshares_ratio_change": stock_data.get("FREESHARES_RATIO_CHANGE"),
        "type_num": stock_data.get("TYPE_NUM")

    }
    InstitutionalHoldingsDAO.add_institutional_holding(stock_hold_data)
    # record = InstitutionalHoldingsDAO.get_holding_by_security_code_and_org_type(stock_data.get("SECURITY_CODE"), stock_data.get("ORG_TYPE"))
    # if record is None:
    #     pass


def fetch_stock_data(date, type):
    params = {
        'date': date,  # 日期
        'type': type,  # 类型
        'zjc': 0,  # 证券简称
        'sortField': "HOULD_NUM",
        'sortDirec': 1,  # 排序方向
        'pageNum': 1,  # 页码
        'pageSize': 50  # 每页大小
    }

    pages = get_pages(params)

    if  pages is not None:
        print(f"总页数: {pages}")
        for i in range(1, pages + 1):
            fetch_data(
                date=date,
                type=type,
                zjc=0,
                sort_field="HOULD_NUM",
                sort_direc=1,
                page_num=i,
                page_size=50
            )
    # 调用函数，传入参数


if __name__ == '__main__':
    # date_list = ['2024-09-30', '2024-06-30', '2024-03-31', '2023-12-31', '2023-09-30', '2023-06-30', '2023-03-31', '2022-12-31', '2022-09-30', '2022-06-30', '2022-03-31', '2021-12-31', '2021-09-30', '2021-06-30', '2021-03-31', '2020-12-31', '2020-09-30', '2020-06-30', '2020-03-31', '2019-12-31', '2019-09-30', '2019-06-30', '2019-03-31', '2018-12-31', '2018-09-30', '2018-06-30', '2018-03-31', '2017-12-31', '2017-09-30', '2017-06-30', '2017-03-31', '2016-12-31', '2016-09-30', '2016-06-30', '2016-03-31', '2015-12-31', '2015-09-30', '2015-06-30', '2015-03-31', '2014-12-31', '2014-09-30', '2014-06-30', '2014-03-31', '2013-12-31', '2013-09-30', '2013-06-30', '2013-03-31', '2012-12-31', '2012-09-30']
    date_list = ['2024-09-30', '2024-06-30', '2024-03-30', '2023-12-30', '2023-09-30', '2023-06-30', '2023-03-30', '2022-12-30', '2022-09-30', '2022-06-30', '2022-03-30', '2021-12-30', '2021-09-30', '2021-06-30', '2021-03-30', '2020-12-30', '2020-09-30', '2020-06-30', '2020-03-30', '2019-12-30', '2019-09-30', '2019-06-30', '2019-03-30', '2018-12-30', '2018-09-30', '2018-06-30', '2018-03-30', '2017-12-30', '2017-09-30', '2017-06-30', '2017-03-30', '2016-12-30', '2016-09-30', '2016-06-30', '2016-03-30', '2015-12-30', '2015-09-30', '2015-06-30', '2015-03-30', '2014-12-30', '2014-09-30', '2014-06-30', '2014-03-30', '2013-12-30', '2013-09-30', '2013-06-30', '2013-03-30', '2012-12-30', '2012-09-30', '2012-06-30', '2012-03-30', '2011-12-30', '2011-09-30', '2011-06-30', '2011-03-30', '2010-12-30', '2010-09-30', '2010-06-30', '2010-03-30', '2009-12-30', '2009-09-30', '2009-06-30', '2009-03-30', '2008-12-30', '2008-09-30', '2008-06-30', '2008-03-30', '2007-12-30', '2007-09-30', '2007-06-30', '2007-03-30', '2006-12-30', '2006-09-30', '2006-06-30', '2006-03-30', '2005-12-30', '2005-09-30', '2005-06-30', '2005-03-30', '2004-12-30', '2004-09-30', '2004-06-30', '2004-03-30', '2003-12-30', '2003-09-30', '2003-06-30', '2003-03-30', '2002-12-30', '2002-09-30', '2002-06-30', '2002-03-30', '2001-12-30', '2001-09-30', '2001-06-30', '2001-03-30', '2000-12-30', '2000-09-30', '2000-06-30', '2000-03-30', '1999-12-30', '1999-09-30', '1999-06-30', '1999-03-30', '1998-12-30', '1998-09-30', '1998-06-30', '1998-03-30', '1997-12-30', '1997-09-30', '1997-06-30', '1997-03-30', '1996-12-30', '1996-09-30', '1996-06-30', '1996-03-30', '1995-12-30', '1995-09-30', '1995-06-30', '1995-03-30', '1994-12-30', '1994-09-30', '1994-06-30', '1994-03-30', '1993-12-30', '1993-09-30', '1993-06-30', '1993-03-30']



    for date in date_list:
        for i in range(1, 7):
            try:
                fetch_stock_data(date, i)
            except Exception as e:
                print(f"请求失败: {e}")

    # fetch_stock_data('2018-06-30')

    # 输出结果
    # if result:
    #     print(result)
