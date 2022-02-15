from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

do_segment(Segment("../../Screen/进入iQIYI设置画面.tcs"))

touch(Template("../../Design/OnlineVideo_favourite_delete_icon.png"), threshold=0.96, timeout=2)
