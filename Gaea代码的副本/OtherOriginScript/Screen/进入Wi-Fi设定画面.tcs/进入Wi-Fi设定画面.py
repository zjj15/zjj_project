from autost.api import *

if exists(Template('../../Design/SettingBar_wifi_focus.png'), timeout=3):
    pass
else:
    do_segment(Segment('../迁移到中控设定画面.tcs'))

    touch([248, 161])

    flick_to(Template('../../Design/SettingBar_wifi_nofocus.png'), [300, 325], DIR_DOWN, step=1, speed=SPEED_NORMAL)

    touch_if(Template('../../Design/SettingBar_wifi_nofocus.png'), timeout=3)

try:
    assert_exists(Template('../../Design/SettingBar_wifi_focus.png'))
    assert_exists(Template('../../Design/Setting_Wifi.png'))
except:
    error('IntoWifiSetting Error!')
