from crawel.charles.piaoxingqiu.performance.create_order import handle_create_order
from crawel.charles.piaoxingqiu.performance.pre_order import handle_pre_order

# 票星球购买脚本，指定观影人，购买指定场次的演唱会
default_audience = ['67666b1ed79e180001e964da', '676544840eb02f0001c8358a']
show_id = '66e5231c607c5e00018d147b'
session_id = '66e5233b9d2c4a0001aa5d3f'
origin_data, supportDeliveries = handle_pre_order(show_id, session_id, len(default_audience))
if origin_data is not None:
    handle_create_order(show_id, session_id, origin_data, default_audience, supportDeliveries)
