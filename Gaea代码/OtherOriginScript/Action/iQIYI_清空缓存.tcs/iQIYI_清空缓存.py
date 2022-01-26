from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

if poco('清除系统缓存', text='清除系统缓存', timeout=1.5).exists():
    poco('是', text='是').click()
    sleep(5)
else:
    do_segment(Segment('../../Screen/进入iQIYI设置画面.tcs'))
    touch_if(Template('../../Design/OnlineVideo_favourite_delete_icon.png'), timeout=2, device=DEV1)
    if poco('清除系统缓存', text='清除系统缓存', timeout=1.5).exists():
        poco('是', text='是').click()
        sleep(5)

touch_if(Template('../../Design/OnlineVideo_return_icon.png'), timeout=2, device=DEV1)
