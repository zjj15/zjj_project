from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)


touch_if(Template('../../../Design/Ons_Memory_查看详情btn.png'), device=DEV1,timeout=100.0, threshold=0.91)
sleep(3)

# wait for hu fully start
for _ in range(15):
    if exists(Template('../../../Design/Ons_Memory_查看详情btn.png'), device=DEV1,timeout=5, threshold=0.91):
        sleep(5)
        touch_if(Template('../../../Design/Ons_Memory_查看详情btn.png'), device=DEV1,timeout=5,threshold=0.91)
    else:
        break
 