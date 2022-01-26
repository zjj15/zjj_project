from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

do_segment(Segment('../../Screen/进入iQIYI我的收藏画面.tcs'))

if poco('清空', text='清空', timeout=2).exists():
    poco('清空', text='清空').click()
