from autost.api import *
#utf-8
DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

assert_exists(Template('../../../Design/StorageFull_title.png'), device=DEV1,timeout = 60)
assert_exists(Template('../../../Design/StorageFull_text.png'), device=DEV1)
