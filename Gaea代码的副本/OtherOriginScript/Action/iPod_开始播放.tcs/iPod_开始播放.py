from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
for i in range(3):
    touch_if(Template('../../Design/USBAudio_PauseButton.png'), timeout=2)
    if exists(Template('../../Design/USBAudio_PlayBar.png'), timeout=2):
        break
else:
    error('iPod Play Error!s')
