from autost.api import *

DEV1= 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
for _ in range(2):
    if poco('最近搜索', text='最近搜索', timeout=1.5).exists() or poco('热门搜索', text='热门搜索', timeout=1.5).exists():
        touch_if(Template("../../Design/OnlineVideo_PlayScreen_return.png"), threshold=0.90, device=DEV1)
    else:
        break