from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

flick([238, 667], DIR_DOWN, step=1, speed=SPEED_NORMAL,device=DEV1)
## fix：ons弹出，touch 失败
for _ in range(3):
    touch_if(Template('../../Design/sound_effect_setting_not_selected_icon.png'), timeout=3,device=DEV1)

try:
    assert_exists(Template('../../Design/sound_effect_setting_selected_icon.png'),device=DEV1)
except:
    error('Into sound effect setting error!')
