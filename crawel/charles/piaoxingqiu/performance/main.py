from crawel.charles.piaoxingqiu.constants.piao_contants import PiaoConstans
from crawel.charles.piaoxingqiu.performance.create_order import handle_create_order
from crawel.charles.piaoxingqiu.performance.pre_order import handle_pre_order, get_can_buy_seat_plan
from crawel.charles.piaoxingqiu.performance.seat_plan_list import fetch_seat_plan_list

# 票星球购买脚本，指定观影人，购买指定场次的演唱会

show_id = '67d6dc4499c2e800011bfa0f'
session_id = '67d6dcd982f5d6000104950b'
seat_plan_list = fetch_seat_plan_list(show_id, session_id)
can_buy_seat_plan = get_can_buy_seat_plan(seat_plan_list, len(PiaoConstans.hong_yan))

if can_buy_seat_plan is not None:
    origin_data, supportDeliveries = handle_pre_order(show_id, session_id, len(PiaoConstans.hong_yan))
    if origin_data is not None:
        handle_create_order(show_id, session_id, origin_data, PiaoConstans.hong_yan, supportDeliveries)
else:
    origin_data, supportDeliveries = handle_pre_order(show_id, session_id, len(PiaoConstans.default_audience))
    if origin_data is not None:
        handle_create_order(show_id, session_id, origin_data, PiaoConstans.default_audience, supportDeliveries)

