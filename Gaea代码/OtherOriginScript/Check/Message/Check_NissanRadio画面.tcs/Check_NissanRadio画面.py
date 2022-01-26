from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__½Å±¾Ãû³Æ: " + __file__)

assert_exists(Template('../../Design/Radio_Nissan_button_focus.png'), device=DEV1)
