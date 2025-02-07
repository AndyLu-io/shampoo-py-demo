from datetime import datetime, timedelta
import calendar

def generate_date_list(start_year, end_year):
# 初始化开始日期和结束日期
    start_date = datetime(start_year, 9, 30)
    end_date = datetime(end_year, 3, 30)

# 存储所有生成的日期
    dates = []

    # 循环直到达到结束日期
    current_date = start_date
    while current_date >= end_date:
        # 将当前日期以 'YYYY-MM-DD' 格式添加到列表
        dates.append(current_date.strftime('%Y-%m-%d'))

        # 减去3个月
        month = current_date.month - 3
        if month <= 0:
            month += 12
            current_date = current_date.replace(year=current_date.year - 1, month=month)
        else:
            current_date = current_date.replace(month=month)

    return dates

# 输出结果
days = generate_date_list(2024, 1993)
print(days)
