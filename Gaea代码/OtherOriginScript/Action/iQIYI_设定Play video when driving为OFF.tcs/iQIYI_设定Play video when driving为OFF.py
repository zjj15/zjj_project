from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
touch_if(Template("../../Design/OnlineVideo_Login_cancel.png"), timeout=1)
flick([1000, 300], DIR_UP, step=3, speed=SPEED_NORMAL,device=DEV1)
flick([1000, 300], DIR_UP, step=3, speed=SPEED_NORMAL,device=DEV1)

if exists(Template('../../Design/play_video_setting_on_icon.png'), timeout=3,device=DEV1):
    touch_in(Template('../../Design/setting_on_icon.png'),Template('../../Design/play_video_setting_on_icon.png'), device=DEV1)

try:
    assert_exists(Template('../../Design/play_video_setting_off_icon.png'),device=DEV1)
except:
    error('set play video setting off fail!') 

