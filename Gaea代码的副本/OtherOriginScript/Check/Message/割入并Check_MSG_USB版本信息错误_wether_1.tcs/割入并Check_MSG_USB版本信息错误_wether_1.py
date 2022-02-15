from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

do_segment(Segment('../../../Action/Message/USB_Switch_IN1_to_none.tcs'))
touch([1026, 55],device=DEV1)
do_segment(Segment('../../../Action/Message/USB_Switch_IN1_to_1.tcs'))
#wait_for_disappearance(Template('../../../Design/MSG_USB版本信息错误_weather.png'), device=DEV1,timeout=5)

assert_exists(Template('../../../Design/usb_version_error.png'), device=DEV1)
