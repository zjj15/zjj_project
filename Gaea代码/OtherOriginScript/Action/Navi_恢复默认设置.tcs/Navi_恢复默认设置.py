from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

touch_if(Template('../../Design/Navi_menu_back.png'), timeout=3)
touch_if(Template('../../Design/Navi_menu_back.png'), timeout=3)
touch_if(Template('../../Design/Navi_mine_button.png'), timeout=3, threshold=0.90)

touch_if(Template('../../Design/Navi_mine_button_夜.png'), timeout=3, threshold=0.90)

touch(Template('../../Design/Navi_setting_icon.png'), threshold=0.93)
touch(Template('../../Design/Navi_setting_other_button.png'), threshold=0.93)

flick([1100, 300], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)
touch(Template('../../Design/Navi_recover_button.png'))
touch(Template('../../Design/Navi_reboot_button.png'))

try:
    assert_exists(Template('../../Design/Navi_Gaode_Tip.png'), threshold=0.93)
except:
    error('Navi revover default setting Error!')
