from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

print("__脚本名称: " + __file__)

# '割入_MSG_设备空间满'
do_segment(Segment('../../../Action/Message/割入_MSG_设备空间满.tcs'))
# 'Check_DisplayOff'
do_segment(Segment('../Check_DisplayOff.tcs'))
sleep(60)
# 'DisplayOff解除'
do_segment(Segment('../../../Action/DisplayOff解除.tcs'))
# 'Check_MSG_设备空间满'
do_segment(Segment('../Check_MSG_设备空间满.tcs'))