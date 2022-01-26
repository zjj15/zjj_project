from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

touch_if(Template('../../../Design/usb_version_error_btn_ok.png'), timeout=3, device=DEV1)
#wait_for_disappearance(Template('../../../Design/usb_version_error.png'), device=DEV1)
