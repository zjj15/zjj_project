from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
if exists(Template('../../Design/sound_setting_beep_off_icon.png'), timeout=3,device=DEV1):
    touch_in(Template('../../Design/setting_off_icon.png'),Template('../../Design/sound_setting_beep_off_icon.png'), device=DEV1)

try:
    assert_exists(Template('../../Design/sound_setting_beep_on_icon.png'),device=DEV1)
except:
    error('set beep on fail!') 
