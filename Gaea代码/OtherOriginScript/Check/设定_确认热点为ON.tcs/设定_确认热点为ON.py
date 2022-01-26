from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'


do_segment(Segment("../../Screen/迁移到中控设定画面.tcs"))
# 进入Wi-Fi设定画面
do_segment(Segment("../../Screen/进入Wi-Fi设定画面.tcs"))
try:
    assert_not_exists(Template('../../Design/hot_point_off_icon.png'),device=DEV1)
except:
    error('check hotspot off fail!') 
