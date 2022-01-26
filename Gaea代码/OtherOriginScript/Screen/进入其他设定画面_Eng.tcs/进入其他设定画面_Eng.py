from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

#进入其他Source

flick([238, 667], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)
# fix：ons弹出，touch 失败
for _ in range(3):
     touch_if(Template('../../Design/otherSetting_English_icon.png'), timeout=3,device=DEV1)

try:
    assert_exists(Template('../../Design/otherSetting_selected_English_icon.png'),device=DEV1)
except:
    error('IntoOtherSetting error!')
