from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

swipe([1087, 667], [1087, 220], step=15, speed=SPEED_NORMAL,device=DEV1)
swipe([1087, 667], [1087, 220], step=15, speed=SPEED_NORMAL,device=DEV1)
touch(Template('../../Design/Setting_Factory_Reset.png'), device=DEV1)
