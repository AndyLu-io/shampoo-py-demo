from crawel.charles.piaoxingqiu.constants.piao_contants import PiaoConstans
from crawel.charles.piaoxingqiu.performance.create_order import handle_create_order
from crawel.charles.piaoxingqiu.performance.pre_order import handle_pre_order, get_can_buy_seat_plan
import datetime
import time
import threading

from crawel.charles.piaoxingqiu.performance.seat_plan_list import fetch_seat_plan_list

# 票星球购买脚本配置
show_id = PiaoConstans.wanglihong_show_id,
session_ids = PiaoConstans.wanglihong_session_ids,

# 设置目标抢票时间
target_time = datetime.datetime(2025, 4, 3, 13, 0, 0)

# 设置线程数（建议 >= session_ids 数量）
THREAD_COUNT = len(session_ids)  # 每个场次分配一个线程

def get_audience(session_id):
    seat_plan_list = fetch_seat_plan_list(show_id, session_id)
    can_buy_seat_plan = get_can_buy_seat_plan(seat_plan_list, len(PiaoConstans.hong_yan))
    if can_buy_seat_plan is not None:
        return PiaoConstans.hong_yan
    else:
        return PiaoConstans.default_audience
def wait_until(target):
    """等待直到目标时间"""
    while True:
        now = datetime.datetime.now()
        if now >= target:
            return
        remaining = (target - now).total_seconds()
        print(f"等待中，距离抢票时间还有 {remaining:.1f} 秒", end='\r')
        time.sleep(0.1)

def attempt_order(thread_id, session_id):
    """单个线程的抢票逻辑，只尝试指定场次"""
    print(f"线程 {thread_id} 开始抢票（场次 {session_id}）...")
    try:
        audience, can_buy_seat_plan = get_audience(session_id)
        origin_data, supportDeliveries = handle_pre_order(show_id, session_id, len(audience), can_buy_seat_plan)
        if origin_data is not None:
            handle_create_order(show_id, session_id, origin_data, audience, supportDeliveries)
            print(f"线程 {thread_id} 抢票成功（场次 {session_id}）！")
        else:
            print(f"线程 {thread_id} 抢票失败（pre_order 返回 None）")
    except Exception as e:
        print(f"线程 {thread_id} 发生错误：{e}")


def main():
    print(f"等待抢票时间: {target_time}")
    wait_until(target_time)

    print("\n开始多线程抢票...")
    threads = []
    for i, session_id in enumerate(session_ids):
        thread = threading.Thread(target=attempt_order, args=(i + 1, session_id))
        thread.start()
        threads.append(thread)

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print("所有线程执行完毕")


if __name__ == "__main__":
    main()