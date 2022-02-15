from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

keyevent(ITCMD_MENU)
keyevent(ITCMD_MENU)

#assert_not_exists(Template('../../Design/statusbar_iqiyi.png'), predict_area=[y,y+h,x,x+w])

assert_not_exists(Template('../../Design/statusbar_iqiyi.png'),threshold=0.9, timeout=5)