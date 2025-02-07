import matplotlib
import pandas as pd

matplotlib.use('TkAgg')  # 或者使用 'Agg', 'Qt5Agg' 等其他后端
import matplotlib.pyplot as plt

from crawel.stock.db.dao.institutional_holdings_dao import InstitutionalHoldingsDAO


def draw_chart(stock_code, type):
    institutional_holdings_dao = InstitutionalHoldingsDAO()

    stock_date_datas = institutional_holdings_dao.list_holding_by_security_code_and_org_type(stock_code, type)
    # 将对象列表转换为 DataFrame

    data = pd.DataFrame([{
        "report_date": item.report_date,
        "security_name_abbr": item.security_name_abbr,
        "hould_num": item.hould_num
    } for item in stock_date_datas])
    # 数据处理
    # 数据处理
    data['report_date'] = pd.to_datetime(data['report_date'])  # 确保日期格式正确
    pivot_data = data.pivot(index='report_date', columns='security_name_abbr', values='hould_num')

    # 绘制图形
    plt.figure(figsize=(10, 6))
    for column in pivot_data.columns:
        plt.plot(pivot_data.index, pivot_data[column], marker='o', label=column)

    plt.title("股票持股数量变化趋势", fontsize=16)
    plt.xlabel("报告日期", fontsize=14)
    plt.ylabel("持股数量", fontsize=14)
    plt.legend(title="股票名称", fontsize=12, loc="best")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


draw_chart('600276', '01')
