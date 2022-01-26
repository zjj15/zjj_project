from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'


for _ in range(10):
    if exists(Template('../../Design/NissanRadio_playing_icon.png'), threshold = 0.95, timeout=1):
        break
    # 式样变更：nissan radio-> ximalaya
    if exists(Template('../../Design/ximalaya_playing_icon.png'), timeout=1):
        break
    elif exists(Template('../../Design/ximalaya_playing_base_1.png'), timeout=1):
        break
    elif exists(Template('../../Design/ximalaya_playing_base_2.png'), timeout=1):
        break
    else:
        continue
else:
    error(__file__+ ' Check error')
