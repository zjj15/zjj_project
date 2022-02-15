from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

"""
case design wrong;
when usb on, vr display.
"""

do_segment(Segment('../../../Action/Message/USB_Switch_IN1_to_none.tcs'))

do_segment(Segment('../../../Common/BackHomeView.tcs'))
touch(Template('../../Design/statusBar_VR_icon.png'),device=DEV1)

do_segment(Segment('../../../Action/Message/USB_Switch_IN1_to_1.tcs'))
assert_exists(Template('../../Design/usb_version_error.png'), device=DEV1)
