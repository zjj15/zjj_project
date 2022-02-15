from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'
#拨号手机
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

do_segment(Segment('../BTHF_来电画面显示.tcs'))
do_segment(Segment('../../Action/BTHF_车机侧点击接听按钮.tcs'))
do_segment(Segment('../../Check/BTHF_确认BT通话中.tcs'))
