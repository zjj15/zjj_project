from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

for i in range(3):
    touch([572, 37], device=DEV1)
    sleep(2)
    if not exists(Template("../../Design/check_displayoff.png"), timeout=3, device=DEV1):
        break
else:
    error(__file__)
