from autost.api import *

#Action
# 手机7：A_MB_0107　号码：17301643089　蓝牙连接车机　连接IDE
# 手机2：S_MB_0569　号码：17301641459 　连接IDE
# 手机3: A_MB_0087： 号码：


#第一部拨号手机DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'
DEV7 = 'iAndroid://127.0.0.1:5037/DRGGAM0860501882'
DialNumber = '17301641459'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

do_segment(Segment('../手机2拨打车机电话_仅拨号.tcs'))
do_segment(Segment('../手机2拨打车机电话_仅呼出.tcs'))
