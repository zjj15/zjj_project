from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
# fix：ons弹出，touch 失败
for _ in range(3):
    flick([238, 667], DIR_DOWN, step=1, speed=SPEED_NORMAL,device=DEV1)
    touch_if(Template('../../Design/displaySetting_icon.png'), timeout=3,device=DEV1)
    if exists(Template('../../Design/displaySetting_selected_icon.png'), timeout=2, device=DEV1):
        break

try:
    assert_exists(Template('../../Design/displaySetting_selected_icon.png'),device=DEV1)
except:
    error('IntoDisplaySetting error!')
