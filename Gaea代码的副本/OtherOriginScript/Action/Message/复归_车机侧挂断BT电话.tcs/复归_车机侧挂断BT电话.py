from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

for i in range(2):
    touch_if(Template('../../../Design/BTHF_Outing_HangUp.png'), timeout=1, device=DEV1)
    touch_if(Template('../../../Design/statusbar_EndCallBtn.png'), timeout=1, device=DEV1)

assert_not_exists(Template('../../../Design/BTHF_Outing_HangUp.png'), device=DEV1, timeout=1)
assert_not_exists(Template('../../../Design/statusbar_EndCallBtn.png'), device=DEV1, timeout=1)
